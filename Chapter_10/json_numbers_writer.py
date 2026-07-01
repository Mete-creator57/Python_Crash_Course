# Learn how to store data permanently 
import json
from pathlib import Path as ph


numbers = [1, 2, 3, 4, 5, 6]
# creating a new file 
# (w+ -> write/read, using this to create the file automatically )
# warning: removes everything that was in the file previously
with open('numbers.json', 'w+', encoding='utf-8') as path:
    # converting numbers to json format using the dumps() method
    contents = json.dumps(numbers)

    # writing to the created json file
    path.write(contents)

# the same as path = Path('numbers.json')

