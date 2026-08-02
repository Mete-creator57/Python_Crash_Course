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

# Get the data
total_repos = f'Total repositories: {response_dict["total_count"]}'
incomplete_results = f'Incomplete results: {response_dict["incomplete_results"]}'
repos = response_dict["items"]
returned_repos_length = len(repos)

first_repo = repos[0]
keys = f'1 repo total keys count: {len(first_repo)}'


print(total_repos)
print(incomplete_results)
print(returned_repos_length)
print(keys)

# loop through the first repo's keys and print them
for key in sorted(first_repo.keys()):
    print(key)




# Output the results
print(response_dict.keys())