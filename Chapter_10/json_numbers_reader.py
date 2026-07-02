import json
from pathlib import Path

# using path/file.loads() method to convert json format
path = Path('numbers.json')
contents = path.read_text(encoding='utf-8')
numbers = json.loads(contents)
print(numbers)
print(numbers[0]+ 10)

# if there is a file in the same dir
file = Path('info.json')

# creating a dict
user_info = {'name': 'mete', 'age': '15'}

# convert the dict to a json format
text = json.dumps(user_info)

# write to a file
file.write_text(text)


# if the fike in the same dir
if file.exists():
    # read from a file and assign to a variable
    contents = file.read_text(encoding='utf-8')

    # convert json format to a dict
    info = json.loads(contents)
    print(info)

    # looping through a dict
    for k, v in info.items():
        print(k, v)

    

