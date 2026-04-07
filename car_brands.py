# Organizing a List / Sorting
cars = ['toyota','bmw','tesla','hyundai','honda','togg','mercedes benz']
print(cars)

cars.sort() # sorting elements in alphabetical order
print("Displaying car brands in alphabetical order")
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == "mercedes benz":
        print(car.title())
    else:
        print(car.capitalize())
        
print(cars)

# sorting in a reverse-alphabetical order by passing "reverse = True" argument
cars.sort(reverse = True)
for car in cars[:6]: # excluding the last element using a slice
    print(car)

# Sorting Elements Temprorarily sorted()
message = "Here's the original list:"
message += f" {cars}"
print(message)

print(f"And here's the sorted list: {sorted(cars)}")

print(f"And again the original list: {cars}")

# Sorting in a reverse order using reverse()
print(f" Before using reverse(): {cars}")
cars.reverse()
print(f" After using reverse(): {cars}")