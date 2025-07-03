# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # Will print: 'Product 2' because case '113' matches product 2.
bar_code_scanner(142)   # Will print: 'Product not found!' because 142 is not the same as '142'. 
