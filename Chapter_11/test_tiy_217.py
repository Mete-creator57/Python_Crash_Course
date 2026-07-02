from tiy_217 import city_country

# City, Country (11-1)
def test_city_country():
    """Test the function workablity"""
    info = city_country('Turkey', 'Istanbul')
    assert info == 'Turkey: Istanbul'

# Population (11-2)
def test_city_country_population():
    """Add the 3rd param to check if the test passes"""
    info = city_country('portugal', 'lisabon', 500000)
    assert info == """Portugal: Lisabon\nPopulation: 500000"""