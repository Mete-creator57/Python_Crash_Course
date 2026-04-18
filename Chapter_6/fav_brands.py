
# A dict of Similar Object
fav_brands = {
    'mete' : 'toyota',
     'jack' : 'nvidia',
     'clark' : 'amd',
     'james': 'apple',
}

print(f"Mete's favorite brand is: {fav_brands['mete'].title()}")

# using get() to access values
sarah = fav_brands.get("sarah",'No values assigned to the specified key')
print(sarah)

# .get(key, default value)
clark = fav_brands.get("clark",'error')
print(clark)
amd = fav_brands.pop("clark")
print(amd)

friends = ['mete', 'jack']

for name, brand in sorted(fav_brands.items()):
    print(f"\n{name.title()}'s favorite brand is: {brand.title()}")
    
    if name in friends:
        print(f"{name.title()} is a friend!")

# Looping Through All the Keys in Dicts
# no need to type keys() method. Loops are looping through all the keys
# by default if no other method is provided when looping through dicts
for name in fav_brands.keys():
    print(name.capitalize())

# Looping Through all the Values in Dicts
for brand in sorted(fav_brands.values()):
    if brand == 'apple':
        print(brand.upper())
    else:
        print(brand.title())

# building a set (no iterated items)
brands = {'toyota','bmw','audi','toyota','honda'}
print(brands)

for brand in brands:
    print(brand)

# using a set while looping through dicts (printing each element only once)
# copying dicts
my_fav_brands = dict(fav_brands)
my_fav_brands['elizabeth'] = 'apple'
print(my_fav_brands)

for brand in set(my_fav_brands.values()):
    print(brand)
    
marketplaces = {
    'sarah' : ['amazon','trendyol'],
    'mete' : ['ptt avm','n11'],
    'jenny': ['trendyol','ptt avm','aliexpress','amazon'],
    'james': ['hepsiburada','aliexpress','neweg'],
    'john': ['aliexpress','temu','neweg'],
    'kate': ['alibaba','neweg'],
}
for index, (name, mps) in enumerate(marketplaces.items()) :
    print(F"\nIndex: {index}, {name.title()} prefers:")
    for mp in mps:
        if mp == 'amazon':
            print(mp.title())
            print(f'-->\tI love {mp.title()} too!')
        else:
            print(f"{mp.title()}") 

copy_dict = marketplaces.copy()
# or
copy_dict_2 = dict(marketplaces)
