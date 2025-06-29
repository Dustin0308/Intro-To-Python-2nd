import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from tkinter import messagebox, filedialog
import requests
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# Database setup
def init_database():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            part_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER NOT NULL,
            min_threshold INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders_out (
            order_id TEXT PRIMARY KEY,
            part_id TEXT,
            quantity INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (part_id) REFERENCES parts (part_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders_in (
            order_id TEXT PRIMARY KEY,
            part_id TEXT,
            quantity INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            supplier TEXT NOT NULL,
            status TEXT NOT NULL,
            tracking_number TEXT,
            est_delivery TEXT,
            FOREIGN KEY (part_id) REFERENCES parts (part_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()

# Database operations
def add_part(part_id, name, category, quantity, min_threshold):
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO parts (part_id, name, category, quantity, min_threshold) VALUES (?, ?, ?, ?, ?)",
            (part_id, name, category, quantity, min_threshold)
        )
        conn.commit()
        conn.close()
        check_low_stock(part_id)
        return True, f"Added part {name}"
    except sqlite3.IntegrityError:
        return False, "Part ID already exists!"

def update_quantity(part_id, quantity_change):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM parts WHERE part_id = ?", (part_id,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        return False, "Part ID not found!"
    current_quantity = result[0]
    new_quantity = current_quantity + quantity_change
    if new_quantity < 0:
        conn.close()
        return False, "Insufficient stock!"
    cursor.execute(
        "UPDATE parts SET quantity = ? WHERE part_id = ?",
        (new_quantity, part_id)
    )
    conn.commit()
    conn.close()
    check_low_stock(part_id)
    return True, f"Updated quantity to {new_quantity}"

def log_outgoing_order(order_id, part_id, quantity, notes):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT part_id FROM parts WHERE part_id = ?", (part_id,))
    if not cursor.fetchone():
        conn.close()
        return False, "Part ID not found!"
    order_date = time.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO orders_out (order_id, part_id, quantity, order_date, status, notes) VALUES (?, ?, ?, ?, ?, ?)",
        (order_id, part_id, quantity, order_date, "Processing", notes)
    )
    conn.commit()
    conn.close()
    success, message = update_quantity(part_id, -quantity)
    if not success:
        return False, message
    return True, f"Logged outgoing order {order_id}"

def place_incoming_order(order_id, part_id, quantity, supplier, api_key, est_delivery):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT part_id FROM parts WHERE part_id = ?", (part_id,))
    if not cursor.fetchone():
        conn.close()
        return False, "Part ID not found!"
    
    try:
        response = requests.post(
            "https://api.supplier.example.com/orders",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"order_id": order_id, "part_id": part_id, "quantity": quantity},
            timeout=5
        )
        if response.status_code != 200:
            return False, f"Supplier API error: {response.text}"
        tracking_number = response.json().get("tracking_number", "TBD")
    except requests.RequestException as e:
        return False, f"API request failed: {str(e)}"
    
    order_date = time.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO orders_in (order_id, part_id, quantity, order_date, supplier, status, tracking_number, est_delivery) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (order_id, part_id, quantity, order_date, supplier, "Ordered", tracking_number, est_delivery)
    )
    conn.commit()
    conn.close()
    return True, f"Placed order {order_id} with {supplier}"

def receive_incoming_order(order_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT part_id, quantity, status FROM orders_in WHERE order_id = ?", (order_id,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        return False, "Order ID not found!"
    part_id, quantity, status = result
    if status == "Received":
        conn.close()
        return False, "Order already received!"
    cursor.execute(
        "UPDATE orders_in SET status = ? WHERE order_id = ?",
        ("Received", order_id)
    )
    conn.commit()
    conn.close()
    success, message = update_quantity(part_id, quantity)
    if not success:
        return False, message
    return True, f"Received order {order_id}: {message}"

def get_shipping_info(tracking_number, api_key):
    try:
        response = requests.get(
            f"https://api.shipper.example.com/track/{tracking_number}",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=5
        )
        if response.status_code != 200:
            return False, f"Shipping API error: {response.text}"
        status = response.json().get("status", "Unknown")
        return True, status
    except requests.RequestException:
        return False, "API request failed"

def check_low_stock(part_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, quantity, min_threshold FROM parts WHERE part_id = ?",
        (part_id,)
    )
    result = cursor.fetchone()
    conn.close()
    if result and result[1] <= result[2]:
        message = f"Low stock: {result[0]} has {result[1]} units left!"
        print(message)
        if PLYER_AVAILABLE:
            notification.notify(title="Low Stock Alert", message=message, timeout=10)
        else:
            messagebox.showwarning("Low Stock Alert", message)

def get_all_parts(search_query="", category_filter=""):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    query = "SELECT part_id, name, category, quantity, min_threshold FROM parts WHERE 1=1"
    params = []
    if search_query:
        query += " AND (part_id LIKE ? OR name LIKE ?)"
        params.extend([f"%{search_query}%", f"%{search_query}%"])
    if category_filter:
        query += " AND category = ?"
        params.append(category_filter)
    cursor.execute(query, params)
    parts = cursor.fetchall()
    conn.close()
    return parts

def get_all_orders_out():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT order_id, part_id, quantity, order_date, status, notes FROM orders_out")
    orders = cursor.fetchall()
    conn.close()
    return orders

def get_all_orders_in():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT order_id, part_id, quantity, order_date, supplier, status, tracking_number, est_delivery FROM orders_in")
    orders = cursor.fetchall()
    conn.close()
    return orders

def save_config(key, value):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def load_config(key, default=""):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM config WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else default

# GUI Application
class PartsManagementApp:
    def __init__(self, root):
        self.root = ttk.Window(themename="flatly")
        self.root.title("Modern Parts Management System")
        self.root.geometry("1200x800")
        
        # Load icons (ensure icons are in the same directory)
        try:
            self.add_icon = ImageTk.PhotoImage(Image.open("add.png").resize((20, 20)))
            self.order_icon = ImageTk.PhotoImage(Image.open("order.png").resize((20, 20)))
            self.refresh_icon = ImageTk.PhotoImage(Image.open("refresh.png").resize((20, 20)))
        except:
            self.add_icon = self.order_icon = self.refresh_icon = None

        # Initialize database
        init_database()

        # Main container
        self.container = ttk.Frame(self.root, padding=10)
        self.container.pack(fill=BOTH, expand=True)

        # Status bar
        self.status_var = ttk.StringVar(value="Ready")
        self.status_bar = ttk.Label(self.container, textvariable=self.status_var, relief=SUNKEN, padding=5)
        self.status_bar.pack(side=BOTTOM, fill=X)

        # Tabs
        self.notebook = ttk.Notebook(self.container)
        self.notebook.pack(fill=BOTH, expand=True, pady=5)

        # Parts Tab
        self.parts_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.parts_frame, text="Inventory")

        # Parts input
        input_frame = ttk.LabelFrame(self.parts_frame, text="Manage Parts", padding=10)
        input_frame.pack(fill=X, pady=5)
        
        ttk.Label(input_frame, text="Part ID:").grid(row=0, column=0, sticky=W, padx=5)
        self.part_id_entry = ttk.Entry(input_frame)
        self.part_id_entry.grid(row=0, column=1, padx=5, pady=5)
        ToolTip(self.part_id_entry, "Unique identifier for the part")

        ttk.Label(input_frame, text="Name:").grid(row=0, column=2, sticky=W, padx=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky=W, padx=5)
        self.category_entry = ttk.Entry(input_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Quantity:").grid(row=1, column=2, sticky=W, padx=5)
        self.quantity_entry = ttk.Entry(input_frame)
        self.quantity_entry.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Min Threshold:").grid(row=2, column=0, sticky=W, padx=5)
        self.threshold_entry = ttk.Entry(input_frame)
        self.threshold_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(
            input_frame, text="Add Part", style="primary.TButton", image=self.add_icon, compound=LEFT,
            command=self.add_part
        ).grid(row=2, column=2, columnspan=2, pady=10)

        # Search and filter
        search_frame = ttk.Frame(self.parts_frame)
        search_frame.pack(fill=X, pady=5)
        ttk.Label(search_frame, text="Search:").pack(side=LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side=LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.update_parts_table)
        ttk.Label(search_frame, text="Category:").pack(side=LEFT, padx=5)
        self.category_filter = ttk.Combobox(search_frame, values=["", "Electronics", "Mechanical", "Other"])
        self.category_filter.pack(side=LEFT, padx=5)
        self.category_filter.bind("<<ComboboxSelected>>", self.update_parts_table)

        # Parts table
        self.parts_tree = ttk.Treeview(
            self.parts_frame,
            columns=("Part ID", "Name", "Category", "Quantity", "Min Threshold"),
            show="headings",
            style="primary.Treeview"
        )
        for col in self.parts_tree["columns"]:
            self.parts_tree.heading(col, text=col, command=lambda c=col: self.sort_treeview(self.parts_tree, c, False))
        self.parts_tree.pack(fill=BOTH, expand=True, pady=5)
        self.parts_tree.bind("<Double-1>", self.edit_part)
        ToolTip(self.parts_tree, "Double-click to edit part")

        # Chart
        chart_frame = ttk.LabelFrame(self.parts_frame, text="Inventory Levels", padding=10)
        chart_frame.pack(fill=X, pady=5)
        self.fig, self.ax = plt.subplots(figsize=(5, 2))
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        # Outgoing Orders Tab
        self.orders_out_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.orders_out_frame, text="Outgoing Orders")

        order_out_input = ttk.LabelFrame(self.orders_out_frame, text="Log Order", padding=10)
        order_out_input.pack(fill=X, pady=5)
        ttk.Label(order_out_input, text="Order ID:").grid(row=0, column=0, sticky=W, padx=5)
        self.order_out_id_entry = ttk.Entry(order_out_input)
        self.order_out_id_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(order_out_input, text="Part ID:").grid(row=0, column=2, sticky=W, padx=5)
        self.order_out_part_id_entry = ttk.Entry(order_out_input)
        self.order_out_part_id_entry.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(order_out_input, text="Quantity:").grid(row=1, column=0, sticky=W, padx=5)
        self.order_out_quantity_entry = ttk.Entry(order_out_input)
        self.order_out_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(order_out_input, text="Notes:").grid(row=1, column=2, sticky=W, padx=5)
        self.order_out_notes_entry = ttk.Entry(order_out_input)
        self.order_out_notes_entry.grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(
            order_out_input, text="Log Order", style="primary.TButton", image=self.order_icon, compound=LEFT,
            command=self.log_outgoing_order
        ).grid(row=2, column=0, columnspan=4, pady=10)

        self.orders_out_tree = ttk.Treeview(
            self.orders_out_frame,
            columns=("Order ID", "Part ID", "Quantity", "Order Date", "Status", "Notes"),
            show="headings",
            style="primary.Treeview"
        )
        for col in self.orders_out_tree["columns"]:
            self.orders_out_tree.heading(col, text=col)
        self.orders_out_tree.pack(fill=BOTH, expand=True, pady=5)

        # Incoming Orders Tab
        self.orders_in_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.orders_in_frame, text="Incoming Orders")

        order_in_input = ttk.LabelFrame(self.orders_in_frame, text="Place Order", padding=10)
        order_in_input.pack(fill=X, pady=5)
        ttk.Label(order_in_input, text="Order ID:").grid(row=0, column=0, sticky=W, padx=5)
        self.order_in_id_entry = ttk.Entry(order_in_input)
        self.order_in_id_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(order_in_input, text="Part ID:").grid(row=0, column=2, sticky=W, padx=5)
        self.order_in_part_id_entry = ttk.Entry(order_in_input)
        self.order_in_part_id_entry.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(order_in_input, text="Quantity:").grid(row=1, column=0, sticky=W, padx=5)
        self.order_in_quantity_entry = ttk.Entry(order_in_input)
        self.order_in_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(order_in_input, text="Supplier:").grid(row=1, column=2, sticky=W, padx=5)
        self.supplier_entry = ttk.Entry(order_in_input)
        self.supplier_entry.grid(row=1, column=3, padx=5, pady=5)
        ttk.Label(order_in_input, text="Est. Delivery (YYYY-MM-DD):").grid(row=2, column=0, sticky=W, padx=5)
        self.est_delivery_entry = ttk.Entry(order_in_input)
        self.est_delivery_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(
            order_in_input, text="Place Order", style="primary.TButton", image=self.order_icon, compound=LEFT,
            command=self.place_incoming_order
        ).grid(row=3, column=0, columnspan=4, pady=10)

        receive_input = ttk.LabelFrame(self.orders_in_frame, text="Receive Order", padding=10)
        receive_input.pack(fill=X, pady=5)
        ttk.Label(receive_input, text="Order ID:").grid(row=0, column=0, sticky=W, padx=5)
        self.receive_order_id_entry = ttk.Entry(receive_input)
        self.receive_order_id_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(
            receive_input, text="Receive Order", style="success.TButton", image=self.order_icon, compound=LEFT,
            command=self.receive_incoming_order
        ).grid(row=0, column=2, padx=5, pady=5)

        self.orders_in_tree = ttk.Treeview(
            self.orders_in_frame,
            columns=("Order ID", "Part ID", "Quantity", "Order Date", "Supplier", "Status", "Tracking", "Est. Delivery"),
            show="headings",
            style="primary.Treeview"
        )
        for col in self.orders_in_tree["columns"]:
            self.orders_in_tree.heading(col, text=col)
        self.orders_in_tree.pack(fill=BOTH, expand=True, pady=5)

        # Settings Tab
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")

        settings_input = ttk.LabelFrame(self.settings_frame, text="API Configuration", padding=10)
        settings_input.pack(fill=X, pady=5)
        ttk.Label(settings_input, text="Supplier API Key:").grid(row=0, column=0, sticky=W, padx=5)
        self.supplier_api_key_entry = ttk.Entry(settings_input)
        self.supplier_api_key_entry.insert(0, load_config("supplier_api_key"))
        self.supplier_api_key_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(settings_input, text="Shipping API Key:").grid(row=1, column=0, sticky=W, padx=5)
        self.shipping_api_key_entry = ttk.Entry(settings_input)
        self.shipping_api_key_entry.insert(0, load_config("shipping_api_key"))
        self.shipping_api_key_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(
            settings_input, text="Save Settings", style="primary.TButton",
            command=self.save_settings
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Refresh button
        refresh_frame = ttk.Frame(self.container)
        refresh_frame.pack(fill=X, pady=5)
        self.progress = ttk.Progressbar(refresh_frame, mode="indeterminate")
        self.progress.pack(side=LEFT, padx=5)
        ttk.Button(
            refresh_frame, text="Refresh Shipping", style="info.TButton", image=self.refresh_icon, compound=LEFT,
            command=self.refresh_shipping_info
        ).pack(side=LEFT, padx=5)

        # Keyboard shortcuts
        self.root.bind("<Control-s>", lambda e: self.save_settings())
        self.root.bind("<Control-r>", lambda e: self.refresh_shipping_info())

        # Auto-refresh
        self.update_tables()
        self.root.after(10000, self.periodic_update)

    def add_part(self):
        part_id = self.part_id_entry.get().strip()
        name = self.name_entry.get().strip()
        category = self.category_entry.get().strip()
        try:
            quantity = int(self.quantity_entry.get())
            min_threshold = int(self.threshold_entry.get())
        except ValueError:
            self.status_var.set("Error: Quantity and Min Threshold must be numbers!")
            return
        if not part_id or not name:
            self.status_var.set("Error: Part ID and Name are required!")
            return
        if quantity < 0 or min_threshold < 0:
            self.status_var.set("Error: Quantity and Min Threshold cannot be negative!")
            return
        success, message = add_part(part_id, name, category, quantity, min_threshold)
        self.status_var.set(message)
        if success:
            self.part_id_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.category_entry.delete(0, END)
            self.quantity_entry.delete(0, END)
            self.threshold_entry.delete(0, END)
            self.update_tables()

    def log_outgoing_order(self):
        order_id = self.order_out_id_entry.get().strip()
        part_id = self.order_out_part_id_entry.get().strip()
        try:
            quantity = int(self.order_out_quantity_entry.get())
        except ValueError:
            self.status_var.set("Error: Quantity must be a number!")
            return
        notes = self.order_out_notes_entry.get().strip()
        if not order_id or not part_id or quantity <= 0:
            self.status_var.set("Error: Order ID, Part ID, and positive Quantity are required!")
            return
        success, message = log_outgoing_order(order_id, part_id, quantity, notes)
        self.status_var.set(message)
        if success:
            self.order_out_id_entry.delete(0, END)
            self.order_out_part_id_entry.delete(0, END)
            self.order_out_quantity_entry.delete(0, END)
            self.order_out_notes_entry.delete(0, END)
            self.update_tables()

    def place_incoming_order(self):
        order_id = self.order_in_id_entry.get().strip()
        part_id = self.order_in_part_id_entry.get().strip()
        try:
            quantity = int(self.order_in_quantity_entry.get())
        except ValueError:
            self.status_var.set("Error: Quantity must be a number!")
            return
        supplier = self.supplier_entry.get().strip()
        est_delivery = self.est_delivery_entry.get().strip()
        if not order_id or not part_id or not supplier or quantity <= 0:
            self.status_var.set("Error: Order ID, Part ID, Supplier, and positive Quantity are required!")
            return
        api_key = load_config("supplier_api_key")
        if not api_key:
            self.status_var.set("Error: Supplier API key not configured!")
            return
        success, message = place_incoming_order(order_id, part_id, quantity, supplier, api_key, est_delivery)
        self.status_var.set(message)
        if success:
            self.order_in_id_entry.delete(0, END)
            self.order_in_part_id_entry.delete(0, END)
            self.order_in_quantity_entry.delete(0, END)
            self.supplier_entry.delete(0, END)
            self.est_delivery_entry.delete(0, END)
            self.update_tables()

    def receive_incoming_order(self):
        order_id = self.receive_order_id_entry.get().strip()
        if not order_id:
            self.status_var.set("Error: Order ID is required!")
            return
        success, message = receive_incoming_order(order_id)
        self.status_var.set(message)
        if success:
            self.receive_order_id_entry.delete(0, END)
            self.update_tables()

    def refresh_shipping_info(self):
        self.progress.start()
        self.status_var.set("Refreshing shipping info...")
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, tracking_number FROM orders_in WHERE status
