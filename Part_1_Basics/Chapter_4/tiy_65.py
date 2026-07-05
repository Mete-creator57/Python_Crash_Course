
# Slices (4-10)
users = ['Mitchel','Mete','John','Cormack','Carter','Zack']

first_three = users[:3]
middle_three = users[2:5]
last_three = users[2:]
print(f"The first three users are: {first_three}")
print(f"The middle three users are: {middle_three}")
print(f"The last three users are: {last_three}")

# My Pizzas, Your Pizzas
pizzas = ['pepperoni','margarita','american','african']
friend_pizzas = pizzas[:]

print(friend_pizzas)
print(pizzas)

pizzas.insert(0,"argentinian")
friend_pizzas.insert(0,"italian")

print(f"\n{friend_pizzas}")
print(f"\n{pizzas}")

for pizza in pizzas:
    print(pizza)

print(f"\n")

for pizza in friend_pizzas:
    print(pizza)

# More Loops (4-12)
# already have been practiced a lot