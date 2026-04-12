# Working with Lists
# 
car_brands = ["Tesla","Honda","Toyota", "Bugatti", "hyindai","Togg","Seat"]

print(car_brands)
print(f"{car_brands[0]} is my favorite car brand!")

# using capitalize() fucntion to print "hyundai" with a capital letter
print(f"{car_brands[4].capitalize()} is trash")
print(f"I'd like to own {car_brands[3]}")




# Practice (page 36)
# create and initialize a list
names = ["Michael","Mitchel","Grace","Clara","Mete"] 
print(names)

print(f"How are you doing, {names[0]}?")
print(f"How are you doing, {names[1]}?")
print(f"How are you doing, {names[2]}?")
print(f"How are you doing, {names[3]}?")
print(f"How are you doing, {names[4]}?")

# add elements to the list 
# append() function adds elements to the end of a list
names.append("George")
print(f"Appending George: {names}")

# insert() function adds elements to any postion of a list
names.insert(3, "Daniel")
print(f"Inserting Daniel: {names}")



# Removing Elements

# using del statement (permanently)
print(names)
del names[2]
print(names)

# using pop() method
consoles = ["playstation","xbox",'nintendo','steam deck','dendy','steam machine']
print(consoles)

first_one = consoles.pop(0) # removing ps (passing argument in parentheses to indicate what item has to be removed)
print(f"{first_one.title()} has been removed from the list")
print(consoles)

# using remove() method
bad = 'nintendo'
consoles.remove(bad)
print(f"{bad.capitalize()} has been removed from the list")
print(consoles)



