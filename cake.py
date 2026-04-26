
# Passing an Arbitary Number of Arguments
def make_cake(size=8, *fillings):
    """Printing a list of prefered fillings of a cake."""
    cake = []

    print('\nProvided fillings are: ')

    # if param is empty
    if not fillings:
        print('No fillings provided...')
        print(f'\n')
        return 


    print('Making your cake...')
    print(f"Cake's size: {size}-inch")
    for i, filling in enumerate(fillings):
        #  making index start form 1, not 0
        print(f"Filling {i + 1}: {filling.title()}")
        cake.append(filling.title())
    
    print(f"Cake's fillings: {cake}")

user_here = True
# initializing an empty list for storing fillings
fillings = []

while user_here:
    filling = input('Enter a desired filling (press q to exit): ')

    if filling == 'q':
        break
    
    # if filling == ''
    elif not filling:
        print('Invalid input. Try again ')
        print(repr(filling))
        continue
    
    fillings.append(filling)

    again = input('Want to add another filling? (Y/N): ')
    if again == 'N':
        break

make_cake(*fillings)
make_cake('versatile buttercream','chocolate ganache', 
'tangy cream cheese')

    
# Mixing Postional and Arbitrary Arguments
make_cake(10, 'cream cheese frosting','cream cheese')


