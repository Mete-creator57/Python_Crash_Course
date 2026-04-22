
# Deli (7-8)
sandwich_orders = ['Grilled Cheese','Reuben','Club Sandwich','Tuna Melt']

# No Pastrami (7-9) --> adding 3 pastramis
for pastrami in range(3):
    sandwich_orders.append('pastrami')

print(sandwich_orders)


# removing all the pastramis
print('The deli has ran out of pastrami...')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

finished_sandwiches = []

for i, sandwich in enumerate(sandwich_orders):
    i += 1
    if sandwich == len(sandwich_orders) - 1:
        print('The last sandwich...')

    else:
          print(f'{i}: Making your {sandwich} sandwich...')
          finished_sandwiches.append(sandwich)
  
print(f'\n')
print('Finished sandwiches: ')
for sandwich in finished_sandwiches:
    print(sandwich)


# Dream Vacation (7-10)

is_active = True
places = []
while is_active:
    question = 'If you could visit any place in this world,'
    question += ' what would it be? '

    place = input(question)
    places.append(place)
    
    print(f'{place.title()} is a great place to visit! ')
    
    next = input('Press Y if want to continue, Press N if want to exit: ')

    if next == 'Y':
        continue

    elif next == 'N':
        print('Bye..')
        break

    else:
        print('Invalid input')
        break

print("Here are the results of the places you'd like to visit: ")
for place in places:
    print(place.title())







    
   
