
# Passing A list as a parameter
# Modifying a list in a function
def greet_users(users):
    for i, user in enumerate(users):
        i += 1
        print(f'{i}: Hello, {user.title()}')

        if user == 'Mete':
            users.append('george'.title())
            print(f"{user.title()} has a friend named {users[4]}!")
            


users = ['Mete','Jenny','Kate','James']
greet_users(users)
print(users)

# Preventing a Function from Modifying a List (using a slice)
# by making a copy of a list
grades = [60, 90, 92]

def show_grades(grades):
     print('Grades are: ')
     for grade in grades:
        print(grade)
    

show_grades(grades[:])

# trying passing a dict as a parameter
def show_points(points):
    print('The points of the lessons are: ')

    for lesson, grade in points.items():
        print(f"\n{lesson.title()}: {grade} out of 100")
        if grade < 70 and grade >= 0:
            print('You failed!')
        elif grade >= 90:
            print('You succeed!')
        elif grade >= 70 and grade < 90:
            print('Average...')
        else:
            print('Invalid grade...')

points = {
    'math': 45,
    'physics': 70,
    'geometry': 30,
    'literature': 99,
}

show_points(points)


