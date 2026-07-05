
# using the range() function
for value in range(1, 9):
    print(value)

for number in range(1,101):
    print(number)

# prints numbers from 0 through 5
# passing only 1 argument
for digit in range(6):
    print(digit)

# using range() to make a List of Numbers
# using list() function -> useful when you make (convert, transform) something into a list
numbers = list(range(0, 6))
print(numbers)

letters = list("abcd")
print(letters)

for letter in letters[0:4]:
    print(letter)

# all these are the same (just using diffrents approaches)
digits = list([1,2,3,4,5])
digits_2 = list((1,2,3,4,5))
digits_3 = [1,2,3,4,5]

print(digits)
print(digits_2)
print(digits_3)

# passing 3rd argument as a step size (2)
even_numbers = list(range(0, 21, 2)) 
print(even_numbers)

# starting from 1 (since it's an odd number)
# step size (1) like: 1, 3, 5...
odd_numbers = list((range(1,21,2)))
for odd_number in odd_numbers:
    print(odd_number)

numbers = list(range(1,11))
print(numbers)

# initializing the index counter
i = 0

for number in numbers:
    numbers.pop(i) # numbers.pop(1)
    number = number ** 2 # 2 = 2 ** 2
    numbers.insert(i,number) # numbers.insert(0, 4)
    i += 1 # incrementing the value of index counter (1 + 1 = 2) 

print(numbers)

# or we could have done like this:
squares = list([])
for number in range(1,11):
    print(f"\nNumber {number} is in the process...")
    number **= 2  # number = number ** 2
    print(f"Squared: {number}")
    squares.append(number)

print(squares)

min_value = min(squares)
print(min_value)

max_value = max(squares)
print(max_value)

summary = sum(squares)
print(f"Сумма всех чисел: {summary}")