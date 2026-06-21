# importing pathlib library
from pathlib import Path

# Writing to a File = One of the simpliest ways to save data
# __file__ = the path related to a file (letter.txt)
# in short, replacing the long path with __file__ smart object
# .parent = makes Python create the file in the current folder
path = Path(__file__).parent / 'letter.txt'
#      [---- WHERE AM I? ----]   / [NAME OF THE FILE]


# using triple quotes to break 
# down the message into lots of lines
msg = '''Hi, Beck.

I wanter to confess to something...
Call me later...'''

# write to a file
path.write_text(msg, encoding='utf-8')

num_file = Path(__file__).parent / 'numbers.txt'

numbers = 3090290948920932

# always convert numerical values to str
# write_text() accepts only str's as arguments
num_file.write_text(str(numbers))

binary_file = Path('test.bin') 
data = b'\x48\x65\x6c\x6c\x6f' 

binary_file.write_bytes(data)