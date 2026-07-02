
# make the population argument optional
def city_country(country, city, population: int = 0):
    """The function which accepts 2 - 3 params"""
    if population:
        info = f"""{country.title()}: {city.title()}\nPopulation: {population}"""
    else:
        info = f"""{country.title()}: {city.title()}"""
    
    return info
