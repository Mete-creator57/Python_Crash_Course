
# Sandwiches (8-12)
items = []
# using an arbitrary number of arguments
def make_sandwich(size, *items, color='white'):
    """Printing every single detail about prepared sandwich"""
    print(f'Making your {size}-inches sized sandwich...')
    print(f'Color: {color.title()}')
    
    print('Items on a sandwich: ')
    for item in items:
        print(f"- {item.title()}")


  
while True:
    print('Press q so as to exit')
    item = input('Enter a desired item on a sandwich: ')

    if item == 'q':
        break

    elif item == '':
        continue
    
    items.append(item)

    next = input('Any other desired items? (Y/N): ')
    if next == 'N' or 'q':
        break

make_sandwich(4, *items)