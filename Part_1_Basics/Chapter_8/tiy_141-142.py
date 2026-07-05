
# What does None do? Analog of null in C#. It means that function doesn't return anything

# City Names (8-6)
def city_country(city, country):
    location = f'{city.title()}, {country.title()}'
    return location

print(city_country('istanbul','turkey'))

# Album (8-7)
# here None is used as a default value ('')
def make_album(name, title, number_of_songs=None):
    album = {
        "Artist's name": name.title(),
        "Album's title": title.title(),
    }
    # loopin through dictionary
    for k, v in album.items():
        print(f"{k.capitalize()}: {v.title()}")



print('Enter q to quit...')
is_active = True

# User Albums (8-8)
while is_active:
    artist_name = input("Enter artist's name: ")
    if artist_name == 'q':
        break

    album_title = input("Enter album's title: ")
    if album_title == 'q':
        break

    songs = input("Enter a number of songs: ")
    if songs == 'q':
        break

    # if songs variable store non-numerical value
    elif not songs.isdigit():
        continue
        
    # converting string to int
    songs = int(songs)
    break
        

make_album(title=album_title, name=artist_name,number_of_songs=songs)

make_album(title='The Tortured Poets Department', name='Taylor Swift', number_of_songs=15)

make_album(title='some title', name='mete batir')

make_album('some artist','some album',5)


   