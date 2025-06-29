# This code was made by Grok for educational puposes only. I wanted to see if I could understand the code as I learn. I understand some of it right now, as I'm still in the Intro book. 

import sqlite3
import time
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
            quantity INTEGER NOT NULL,
            min_threshold INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add a new part to the database
def add_part(part_id, name, quantity, min_threshold):
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO parts (part_id, name, quantity, min_threshold) VALUES (?, ?, ?, ?)",
            (part_id, name, quantity, min_threshold)
        )
        conn.commit()
        conn.close()
        check_low_stock(part_id)
        return True, f"Added part {name}"
    except sqlite3.IntegrityError:
        return False, "Part ID already exists!"

# Update quantity in the database
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

# Check for low stock and trigger notification
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
        message = f"Low stock alert: {result[0]} has {result[1]} units left!"
        print(message)
        if PLYER_AVAILABLE:
            notification.notify(
                title="Low Stock Alert",
                message=message,
                timeout=10
            )

# Simulate reordering (extendable to API)
def reorder_part(part_id, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM parts WHERE part_id = ?", (part_id,))
    result = cursor.fetchone()
    conn.close()
    if not result:
        return False, "Part ID not found!"
    # Simulate reorder (replace with API call in production)
    print(f"Reordered {quantity} units of {result[0]} (ID: {part_id})")
    # Update quantity to simulate restock
    success, message = update_quantity(part_id, quantity)
    if success:
        return True, f"Reordered {quantity} units: {message}"
    return False, message

# Get all parts for display
def get_all_parts():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT part_id, name, quantity, min_threshold FROM parts")
    parts = cursor.fetchall()
    conn.close()
    return parts

# Display inventory
def display_inventory():
    parts = get_all_parts()
    if not parts:
        print("No parts in inventory.")
        return
    print("\nInventory:")
    print("Part ID | Name | Quantity | Min Threshold")
    print("-" * 40)
    for part in parts:
        print(f"{part[0]} | {part[1]} | {part[2]} | {part[3]}")

# Console-based menu
def main():
    init_database()
    while True:
        print("\nParts Management System")
        print("1. Add Part")
        print("2. Update Quantity (Order/Restock)")
        print("3. Reorder Part")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            part_id = input("Enter Part ID: ")
            name = input("Enter Part Name: ")
            try:
                quantity = int(input("Enter Quantity: "))
                min_threshold = int(input("Enter Minimum Threshold for Alert: "))
                if quantity < 0 or min_threshold < 0:
                    print("Quantity and Min Threshold cannot be negative!")
                    continue
            except ValueError:
                print("Quantity and Min Threshold must be numbers!")
                continue
            if not part_id or not name:
                print("Part ID and Name are required!")
                continue
            success, message = add_part(part_id, name, quantity, min_threshold)
            print(message)

        elif choice == "2":
            part_id = input("Enter Part ID: ")
            try:
                quantity_change = int(input("Enter Quantity Change (negative for order, positive for restock): "))
            except ValueError:
                print("Quantity change must be a number!")
                continue
            success, message = update_quantity(part_id, quantity_change)
            print(message)

        elif choice == "3":
            part_id = input("Enter Part ID: ")
            try:
                quantity = int(input("Enter Reorder Quantity: "))
                if quantity <= 0:
                    print("Reorder quantity must be positive!")
                    continue
            except ValueError:
                print("Reorder quantity must be a number!")
                continue
            success, message = reorder_part(part_id, quantity)
            print(message)

        elif choice == "4":
            display_inventory()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
