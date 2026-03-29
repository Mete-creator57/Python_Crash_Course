# Personal Message 2-3
name = "eric"
message = f"Hello {name}, let's learn some Python today!"
print(message)

# Name Cases (using diffrent string methods to represent a string) 2-4
full_name = "mete batir tunkiz"
output = f"{full_name.title()} is your name"
print(output)
print(f"{full_name.capitalize()}")
print(full_name.upper())
print(full_name.lower())

# Famous Quote 2-5
famous_name = "nikola tesla"
message = f"{famous_name.title()} once said: I am not scared of electricity"
print(message)

# skipped 2-6

# Stripping Strings 2-7
language = " python "
print(language) # before stripping

print(language.lstrip()) # stripping the left side

print(language.rstrip()) # stripping the right side

print(language.strip()) # stripping both sides

# File Extensions 2-8 removeprefix() = start prefix , removesuffix() = end suffix
url = "https://youtube.com"
print(url.removeprefix("https://")) # prints youtube.com (protocol name removed)

extension = "python.py"
print(extension.removesuffix(".py")) # prints python (file extension removed)