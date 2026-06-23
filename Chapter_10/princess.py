from pathlib import Path as ph


path = ph('The_Princess_and_the_Pea.txt')
try:
# try to read from a file
# assign what's read to a str variable
    path.read_text(encoding='utf-8')

# Handle the error
except FileNotFoundError:
    print('This file is not found in the current directory')

else:
    # Count the approximate number of words in the file
    contents = path.read_text().split()
    total_words = len(contents)
    print(f'The file "{path}" has {total_words} words.')


# Working with Multiple Files
def replace_spaces(add_file):
    '''Replace all whitespaces in a file'''
    
    path = ph(add_file)


    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError as f:
        print('This file is not found in the current folder...')
        print(f)
    else:
        clean_text = contents.replace('\n', ' ')
        print(f'Before: \n{contents}')
        print(f'After: \n{clean_text}')
       
    

replace_spaces('alice.txt')
replace_spaces('bag.txt')