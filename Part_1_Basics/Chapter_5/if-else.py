
# Practicing if-else statements (conditions)
# using an ordinary loop 
brands = ['tesla','Toyota','Bmw','Togg','clio']
fav_brand = 'bmw'

for brand in brands:
    if brand == 'Bmw':
      fav_brand = brand.upper()
      print(fav_brand)
      
      
    else:
      brand = brand.title()
      print(brand)
    
   # using enumerate()

items = ['screwdriver','hammer','wrench','tire']

for index, item in enumerate(items):
    items[index] = item.capitalize()
    print(f"{item} is at index: {index}")
    print(f"Changing this element's value")
    items[index] = 'Changed'
    print(f"{item} --> {items[index]}")

print(items)

taken_passwords = [1234, 5770, 6666]
user_pw = 1234


if user_pw in taken_passwords:
    print('This password is taken!')

elif user_pw not in taken_passwords:
    print("You're welcome!")


