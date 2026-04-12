
# List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

# Analog for this
squares_an = []
for value in range(1,11):
    value **= 2
    squares_an.append(value)

print(squares_an)


# and for this one too
squares_2 = list(range(1,11))

# for INDEX in range(10)
for number in range(len(squares_2[:])):
    squares_2[number] **= 2
    
print(squares_2)
    