from pathlib import Path

# Addition (10-6)

first_num = ''
second_num = ''
while True:
    # checking if users want to continue
    check = input('Press any key to continue or q to leave: ')
    if check.lower() == 'q':
        break

    try:
        first_num = int(input('Enter your first number: '))
        second_num = int(input('Enter your second number: '))
    except ValueError as ve:
        print('Not a numerical input...')
        print('1: '+ repr(first_num))
        print('2: ' + repr(second_num))
        print('You are about to get back to the start...')
        continue

    else:
        result = first_num + second_num
        print(f'The result of the addition: {result}')
        


# Addition Calculator (10-7)
# done

# Cats and Dogs (10-8)
def file_reader(path: str):
    path = Path(__file__).parent / path
    try:
        contents = path.read_text().splitlines()
    except FileNotFoundError:
        print(f"{path} file is not found")
        # failing silently
        pass
    else:
        print('The file ' + str(path))
        for line in contents:
            print(line)
    
    # leaving space
    print()
    
file_reader('cats.txt')
file_reader('dogs.txt')
file_reader('lions.txt')

# Common Words (10-10)
text = 'Hello, My name is Mete. Mete IS a clever boy'
word = 'IS'
times = text.upper().count(word)
print(F"The word {word} was catched {times} times in this string")