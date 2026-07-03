# import from the file in which the class we're testing 
from survey import Survey

def test_show_question():
    """Test if displaying the question works correctly"""
    # define the question
    question = 'What is your main goal to achieve in life?'

    # creating an instance of the class
    survey = Survey(question, 6)

    # Test the func
    check = survey.show_question()
    assert check == True
    
def test_greeting_in_a_list():
    """Test if there is the greetting in a list"""
    survey = Survey('How are you?', 8)
    
    # call the function to insert the greeting
    survey.insert_greeting()
    assert 'The Results: ' in survey.responses

