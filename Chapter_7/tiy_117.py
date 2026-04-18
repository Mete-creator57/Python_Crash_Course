
# Rental Car (7-1)
car = input('What kind of car would you like? ')

print(f"Let me see if I can find you a {car.title()}")

# Restaraunt Seating (7-2)
people_num = int(input('How many people are in the group? '))

if people_num > 8:
    print("You'l have to wait for a table!")
elif people_num <= 0:
    print('There can not be 0 or less people!')
else:
    print("Your table is ready!")

# Multiples of Ten (7-3)
question = input('Enter a random number: ')

if isinstance(question, int) and question % 10 == 0:
    print('Your number is a multiple of 10!')

elif isinstance(question, str):
    print("It's not an actual number!")

else:
    print("Your number is not multiple of 10!")


