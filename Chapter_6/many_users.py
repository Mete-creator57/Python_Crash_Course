
# A dict in a dict

registered_users = {
    # username (a key in a dict)
    'mete123abc' : {
        'first_name':'Mete',
        'last_name':'Tunkiz',
        'location':'Chicago',
         'preferences': ['dark mode','big text'],
        'font': 'arial', 
    },

  'jenn1985@' : {
        'first_name':'jennet',
        'last_name':'bayryyeva',
        'location':'Istanbul',
         'preferences': ['light mode','small text'],
        'font': 'monreal', 
        },

}

# for jenn1985@, all the key-value pairs in a dict
# info = all key-value pairs in dict belong to a username (dict name)
for username, info in registered_users.items():
    print(f'\nUsername: {username}')

    # for 'first_name','jennet'
    for key, value in info.items():
        if key == 'preferences':
            print(f'\t{key.title()}:')
            for preference in info['preferences']:
                print(f"\t{preference.upper()}")
        else:
            print(f'{key.title()}: {value.title()}')

