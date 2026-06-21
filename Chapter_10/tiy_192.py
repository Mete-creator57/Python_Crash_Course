# Guest (10-4)
from pathlib import Path as ph
path = ph(__file__).parent / 'guest_list.txt'

name = input('Type your name: ')
# must be alphabetic and longer than or equal to 3
while not name.isalpha() and len(name) >= 3:
    name = input('Type your name: ')

# write to the createad file
path.write_text(name, encoding='utf-8')

# Guest_Book (10-5)
guests = ph(__file__).parent / 'guests.txt'
is_active = True
# initializing an empty list for storing user's names
names = []
msg = 'Enter your name: '


print('Press Q to exit...')
# creating an endless loop
while is_active:
    name = input(msg)
    if name.upper() == 'Q':
        print('Closing the programm...')
        is_active = False
    else:
        names.append(name)
    

guest_list = ''
# iterate over the list of names
for name in names:
    # assign each element from the list to a str variable 
    # alongside with the comma afterwards
    guest_list += name + ', '



guests.write_text(guest_list, encoding='utf-8')

# test WITH OPEN(), with = closes a file after the end
#  of an operation
message = 'Random text'
#        [file's path] , [action],  encoding      [assigned variable]   
with open('some_text.txt', 'r+', encoding='utf-8') as file:
    # write to a file
    file.write(message)

    # return to the start
    file.seek(0)

    # read from the file and assign it to a variable
    contents = file.read()
    
    # print what's beem read from the file
    print(contents)
    # no need to write file.close() so as to close the file


    
