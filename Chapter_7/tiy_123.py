
# Pizza Toppings (7-4)
pizza = []
while True:
    topping = input('Enter a topping: ')
    if topping == 'quit':
        break
    else:
         print(f'Adding {topping} to your pizza!')
         pizza.append(topping)
    
print(pizza)

fee = 0
is_active = True
# Movie Tickets (7-5)
while is_active:

    age = input('Enter your age: ')

    if age == 'quit':
        is_active = False

    age = int(age)

    if age < 3 and age > 0:
        print('The ticket is free!')
        break

    elif age >= 3 and age <= 12:
        fee = 10
        print(f'The ticket is {fee}$')
        break

    elif age > 12:
        fee = 15
        print(f'The ticket is {fee}$')
        break

    else:
        print('Invalid age')
        continue

# Three Exits (7-6)
# done

# Infinity (7-7)
i = 10
while i <= 20:
    print('Hello Bro')