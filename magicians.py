 # for loop
magicians = ['Clara','Jessica','Mitchel']
for magician in magicians:
    print(f"Hello, {magician}!")


# excluding Mitchel bu using a slice
for magician in magicians[0:2]:
    print("Hello "+ magician + "!")


# Doing More Work Within a for Loop
inventory = ['sword','shield','equipment','granate','bomb']
for item in inventory:
    print(f"{item.title()} is in the inventory")
    print(f"\t{item.capitalize()} can be used \n")

# Doing something after a for Loop
print('Thanks to everyone! Have a nice day!')

