from pathlib import Path

# using the abs path because the text 
# isn't in the same directory as the current file
# using raw strings (with prefix r '')
path = Path(r"D:\Soft_Dev\Python_Crash_Course\texts\pi_digits.txt")

# reading the text from the file and 
# splitting lines (returns the list of lines (strs))
contents = path.read_text().splitlines()
print(contents)

# Looping through the list of lines
for i, line in enumerate(contents, 1):
    # removing all whitespaces from both left and right sides
    line = line.strip()
    print(f'\n{i} line: ' + line)
    print(f'The length of this line: {len(line)}')

# Working with File's Contents
words = path.read_text()
pi_string = ''

# looping through each line 
for line in words.splitlines():
    line = line.strip()
    pi_string += line


print(f'\n{pi_string}', end=' -> ')
print('The length: ' + str(len(pi_string)))
# limiting the string to only 10 characters long
print(pi_string[:10])
