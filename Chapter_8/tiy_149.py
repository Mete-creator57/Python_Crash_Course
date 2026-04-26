
# Sandwiches (8-12)
items = []
# using an arbitrary number of arguments
def make_sandwich(size, *items, color='white'):
    """Printing every single detail about prepared sandwich"""
    print(f'Making your {size}-inches sized sandwich...')
    print(f'Color: {color.title()}')
    
    print('Items on a sandwich: ')
    for item in items:
        print(f"- {item.title()}")


print('Press q so as to exit')
is_active = True
while is_active:
    item = input('Enter a desired item on a sandwich: ')

    if item == 'q':
        break

    elif item == '':
        continue
    
    items.append(item)
    
    while True:
        next = input('Any other desired items? (Y/N): ')
         # if next.upper() == 'N' or next.upper() == 'Q'
        if next.upper() in ('N', 'Q'):
            is_active = False
            break
        else:
            continue
  

make_sandwich(4, *items)

# User Profile (8-13)
def build_profile(username, age, **profile_info):
    """Assigning everything we know about a person"""
    ordered_profile = {
         'username' : username,
         'age' : age,
    }

    ordered_profile.update(profile_info)
   
    
    # returning a dict
    return ordered_profile

me = build_profile(age="15", username='meteshka12',location='Turkiye',
gender='male',adult='no',brands=['Toyota','bugatti','tesla'])

print(me)
# looping through my dict
for key, value in me.items():
    if key == 'brands':
        print(f'{key.title()}')
        for brand in me['brands']:
            print(f'- {brand.title()}')
    else:
        print(f'{key.title()}: {value.title()}')
    

# Cars (8-14)
def make_car(mfg, model, color='blue', **car_info,):
    print(f'Manufacturer: {mfg.title()}')
    print(f'Model: {model.title()}')
    print(f'Color: {color.title()}')

    car = {
        'manufacturer': mfg.title(),
        'model': model.title(),
        'color': color.title()
    }

    car.update(**car_info)
    
    return car

my_car = make_car('toyota','hybrid',max_speed='200', year='early 2021')

for i, (k, v) in enumerate (my_car.items()):
    if k == 'max_speed':
        print(f"{i + 1} - Max Speed: {v.title()} km")
    else:
        print(f"{i + 1} - {k.title()}: {v.title()}")
    
