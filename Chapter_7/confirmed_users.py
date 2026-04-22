
unuath_users = ['mete','jess','clark','John']
auth_users = ['jenny']

# runs as long as unuath_users list is not empty
while unuath_users:
    current_user = unuath_users.pop()

    print(f'Checking user: {current_user}')
    auth_users.append(current_user)

print('These users have been confirmed: ')
for user in auth_users:
    print(user.title())


checked_phones = {

}

unchecked_phones = {
   'vivo': {
    'cpu': 'snap dragron',
    'model': "y18",
    'year': '2024',
    'is rare' : 'no',
    'is flagship': 'no',
    'random words': ['JSDDKS','KDSKSFD','ketchup']
   },
   
   'samsung' : {
    'cpu': 'snap dragron',
    'model': "s24 ultra",
    'year': '2024',
    'is rare' : 'no',
    'is flagship': 'yes',
    'random numbers': [2,2,3,5,23,4221,234,5]

   },
}

for i, (phone_name, phone_info) in enumerate(unchecked_phones.items()):
    print(F"\nIndex: {i}, Phone name: {phone_name.title()}")
    
    for key, value in phone_info.items():
        if key == 'random words':
            print(key.title() + ":")

            for word in phone_info['random words']:
                print(word.title())
                
                
        
        elif key == 'random numbers':
            print(key.title() + ":")
            for number in phone_info['random numbers']:
                print(number)
                
        
        elif isinstance(value,str):
            print(f"{key.title()}: {value.title()}")
            
    
        checked_phones = unchecked_phones.copy()
    
print(checked_phones)

print('Looping through checked phones...')

for checked_phone, info in checked_phones.items():
    print(f'\n Phone: {checked_phone.title()}')

    for key, value in info.items():

        # printing each word
        if key == 'random words':
            print(key.title() + ':')

            for word in info['random words']:
              print(f"\t{word.title()}")
            
            print('END!')
        
        # printing each number
        elif key == 'random numbers':
            print(key.title() + ':')

            for num in info['random numbers']:
                print(num)
            
            print('END!')

        # printing each key-value pair if none of the conditions above are True
        else:
            print(f"{key.title()}: {value.title()}")


    

    
