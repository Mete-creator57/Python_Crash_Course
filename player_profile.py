
# Using Arbitrary Keyword Arguments
# passing a dict as a param (** = tell python to create a dict named gamer_info),
# containing all the extra name-value pairs
def build_gamer(username, age, **gamer_info):
    """Printing everything we know about gamer"""
    gamer_info['username'] = username
    gamer_info['age'] = age
    
    # returning a dict
    return gamer_info

# assigning func call to a variable to return a value
gamer = build_gamer('metehapik123', 15, location='Turkiye', gender='male')

print(gamer)
