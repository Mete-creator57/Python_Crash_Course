# Define a fucntion

def get_formatted_info(name: str, surname: str, country: str, age: int = 0):
    """Generate a neatly formatted name about users"""
    full_name = f"{name.capitalize()} {surname.capitalize()}"
    if age:
        return f"Name: {full_name}, \nAge: {age}, \nCountry: {country}"
    else:
        return f"Name: {full_name}, \nCountry: {country}"
    


