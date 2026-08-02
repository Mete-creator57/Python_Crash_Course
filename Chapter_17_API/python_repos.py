import requests


# Make an API call and check the response from the website
url = 'https://api.github.com/search/repositories'
# :>10000 look for those who have more than 10.000 stars
url += '?q=language:python+sort:stars:>10000' 

# Accept  data only in json format -> 'Accept' 
# using 3rd version of GitHub's API
headers = {'Accept': 'application/vnd.github.v3+json'}

# Request the data using .get() function
#  by passing the url of the website and the headers
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Convert the response object to a dict
response_dict = r.json()

# Output the results
print(response_dict.keys())