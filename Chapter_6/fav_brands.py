
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