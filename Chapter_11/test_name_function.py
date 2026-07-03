# import the created method from the file
from name_function import get_formatted_info

# pytest only checks in the fucntions start with test_...
def test_name_function():
    """Test the function"""
    info = get_formatted_info('Mete', 'tunkiz', 'Turkmenistan')
    print(info)
    # check if 'info' stores the given value
    assert info == f"Name: Mete Tunkiz, \nCountry: Turkmenistan"



def test_another_name():
    text = get_formatted_info('Clark', 'robber', 'USA', 16)
    assert text == f"Name: Clark Robber, \nAge: 16, \nCountry: USA"

# .. will indicate that 2 tests have passed 
