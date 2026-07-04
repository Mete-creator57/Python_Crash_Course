# import pytest module to use it's methods (fixtures)
import pytest
# import from the file in which the class we're testing 
from survey import Survey

# apply the fixture to the method to reuse it
@pytest.fixture
def subjects_survey():
    """A survey that will be used in all test functions"""
    question = 'What is your favorite subject at school?'
    subjects_survey = Survey(question, 7)
    return subjects_survey


def test_show_question():
    """Test if displaying the method returns True"""
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

# pass the returned value (the instance) to the test fuction
def test_school(subjects_survey):
    """Test if the school name is displayed correctly"""
    subjects_survey.school_name = 'Borsa'
    assert subjects_survey.school_name == 'Borsa'
