
# Counting to Twenty (4-3)
# starts counting from 0
for number in range(11):
    print(f"Number {number}")

# One Million (4-4)
# the same as one_million = [1, 2, 3, 4...]
a_million = list(range(1,1000001))

is_active = False

if is_active:
    print("Counting from 1 to a million")
    for number in a_million:
        print(number)



# Summing a Million (4-5)
min_value = min(a_million) 
max_value = max(a_million)
summary = sum(a_million) # summing all values in a list a_million

print(min_value)
print(max_value)
print(summary)

# Odd Numbers (4-6)
print("Printing only odd numbers from 1 to 20")
# passing a third argument as a step size
for odd_number in range(1,21,2):
    print(odd_number)

# Threes (4-7)
multiples_of_three = list(range(3,31,3))

for multiple in multiples_of_three:
    print(multiple)

multiples_three = []
# or we could have done like this
for value in range(3,31):
    if value % 3 == 0:
        print(value)
        multiples_three.append(value)
    else:
        print(f"{value} isn't a multiple of three")
    
print(multiples_three)

# Cubes (4-8)
cubes = []
for digit in range(1,11):
    print(f"Cube of {digit} is {digit**3}")
    cubes.append(digit**3)

print(cubes)

# Cube Comprehension (4-9)
cubes = [number**3 for number in range(1,11)]
print(cubes)