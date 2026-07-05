
import random
# Die (9-13)
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    
    def roll_die(self):
        random_num = random.randint(1, self.sides)
        return random_num
    

die = Die(10)
print(f'Rolling {die.sides}-sided die 10 times')
for i in range(10):
    print(die.roll_die())

die = Die(20)
print(f'Rolling {die.sides}-sided die 10 times')
# looping through a die 10 times
for i in range(10):
    print(die.roll_die())

# Lottery (9-14)
# Lottery Analysis (9-15)
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = '4D85'


print('Any ticket matching the winning ticket, wins 3000$ dollars')

counter = 0
while True:
    counter += 1
    my_ticket = []

# picking elements randomly
    for element in range(4):
        element = random.choice(possibilities)
        my_ticket.append(element)
    
    # joining all elements in a list into a single string
    # because we can't concatenate str to int, we convert each element on each 
    # iteration to str so we can join them together.
    # .join() expects that we provide only str's (list, tuple) as an argument 
    my_ticket = "".join(str(element) for element in my_ticket)

    if my_ticket == winning_ticket:
        print(f"Match! You've got it on a {counter} try!")
        break



    

    



