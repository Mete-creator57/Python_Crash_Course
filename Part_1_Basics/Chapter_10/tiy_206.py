from pathlib import Path
import json

# Favorite Number (10-11)
while True:

    fav_num = input('Enter your favorite number: ')

    try:
        # try to convert user's input to int
        fav_num = int(fav_num)
    except ValueError:
        print('Invalid input')
        continue
    else:
        break

file = Path('fav_num.txt')
fav_num = json.dumps(int(fav_num))
file.write_text(fav_num)

fav_num = file.read_text()
fav_num = json.loads(fav_num)
print('I know your favorite number is ' + str(fav_num))

# Favorite Number Remembered (10-12)
# ...

        


