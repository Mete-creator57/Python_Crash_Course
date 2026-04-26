
# Messages (8-9)
def show_messages(messages):
    for message in messages:
        print(message.capitalize())

messages = ['mete is a programmer','python is an easy language']
show_messages(messages[:])

numbers = [1, 2, 3, 4, 5, 6]
def show_numbers(numbers):
    i = 0
    # taking the first item from a list and assigning it to a variable
    while numbers:
        current_num = numbers.pop(i)
        print(current_num)

# func call
show_numbers(numbers)

# Sending Messages (8-10)
sent_messages = []
messages = ['I like python', 'I like C#']

def send_messages(messages):
    while messages:
        cur_message = messages.pop(0)
        print(cur_message.capitalize())

        sent_messages.append(cur_message)


    print('Sent messages: ')
    print(sent_messages)

    print('Original messages: ')
    print(messages)


send_messages(messages)


# Archived Messages (8-11)
print(f'\n')
sent_messages_2 = []
messages_2 = ['hello bro','hello Mr.Smith']


def send_messages_2(messages_2):
    while messages_2:
        current_message = messages_2.pop(0)
        print(current_message.title())
        sent_messages_2.append(current_message)


send_messages_2(messages_2[:])

print(f"Orig: {messages_2}")
print(f"Sent: {sent_messages_2}")
