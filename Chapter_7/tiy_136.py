
# T-Shirt (8-3)
def make_shirt(size='l',text='i love python'):
    print(f'It is {size.upper()} sized shirt')
    print(f'{text.title()} is written on it')

make_shirt('s','i love you')
print(f'\n')
make_shirt(text='i love you',size='s')

# Large Shirts (8-4)
# modyfiying the function
make_shirt(size='m')
make_shirt()
make_shirt(size='',text='i love c#')

# Cities (8-5)
def describe_city(city_name, country='the usa'):
    print(f"{city_name.title()} is in {country.title()}")

describe_city('istanbul','Turkey')
