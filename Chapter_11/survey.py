# Define a class
class Survey:
    def __init__(self, question, people_count):
        """Store a question, response and people count"""
        self.question = question
        self.responses = []
        self.people_num = people_count

    def show_question(self, greeting='Welcome Everyone!') -> bool:
        """Print the question and the greeting to the screen"""
        print(greeting)
        print(self.question)
        return True
    
    def get_response(self):
        """Get responses from users"""
        person = 0

        while self.people_num: 
            answer = input('Your answer: ')
            self.responses.append(answer)
            self.people_num -= 1
           
            

    def show_result(self):
        '''Print the results'''
        # put the msg to the start

        print('Here are the results: ')

        # loop through a list
        for i, response in enumerate(self.responses, 1):
            print(f'Answer {i}: {response}')
    
    def insert_greeting(self, result='The Results: '):
        """Insert the greeting into a list"""
        self.responses.insert(0, result)
    

