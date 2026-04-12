# Try It Yourself
# Seeing the World (3-8)
places = ["France","Spain","Italy","Mexico","the USA"]

# Original Order
print(places)

# sorting temporarily
print(sorted(places))

print(places)

# sorting temporarily using reverse = True argument withing sorted() method
# sorted(what to sort, how to sort) -> in this case in reverse alphabetical order
print(sorted(places, reverse = True))

print(places)

places.reverse()
print(places)

print(f"\n{places}")

places.sort()
print(places)

places.sort(reverse= True)
print(places)

# Dinner Guests (3-9)
guest_list =['David','Clark','Julia','Robert']
guest_number= len(guest_list)
if guest_number == 1:
     print(f"Only {guest_number} person is coming for dinner")
elif guest_number == 0:
    print(f"No one is coming for dinner")
else:
    print(f"{guest_number} people are coming for dinner")

# Every Function (3-10)
languages = ['English','Russian','Jewish','Arabic','German','Japanese']
the_most_popular = languages.pop(0)
print(the_most_popular)

del languages[2]

languages.remove('Russian')

len(languages)

# sorting them in alphabetical order
languages.sort() 

# reverse alphabetical order
languages.sort(reverse = True)

# sorting temporarily
print(sorted(languages))

# sorted() fucntion can accept reverse = True as an argument as well
print(sorted(languages, reverse = True))

print(languages)


