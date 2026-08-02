import requests
import plotly.express as px

# Make an API call and check the response from the website
url = 'https://api.github.com/search/repositories'
# :>10000 look for those who have more than 10.000 stars

# Accept  data only in json format -> 'Accept' 
# using 3rd version of GitHub's API
headers = {'Accept': 'application/vnd.github.v3+json'}

# 2. Define API query parameters as a dictionary.
# Using 'params' lets Python safely handle encoding (no accidental spaces!)
query_params = {
    # Combine the language and star filter inside the 'q' parameter string:
    'q': 'language:python stars:>10000',
    # Explicitly set sorting parameters separately:
    'sort': 'stars',
    'order': 'desc' # get with the most stars first
}
# Request the data using .get() function
#  by passing the url of the website and the headers
r = requests.get(url, params=query_params,  headers=headers)
print(f'Status code: {r.status_code}')

# Convert the response object to a dict
response_dict = r.json()

# Get the data
total_repos = f'Total repositories: {response_dict["total_count"]}'
incomplete_results = f'Incomplete results: {response_dict["incomplete_results"]}'
repos = response_dict["items"]
returned_repos_length = len(repos)

repo_names, stars = [], []
for repo in repos:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

print(total_repos)
print(incomplete_results)
print(returned_repos_length)



# Loop through first 30 repos
print('\n Info about each repo')
for repo in repos[:30]:
    print(f"Name: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Watchers: {repo['watchers']}")
    print()

# Visualize the results
fig = px.bar(x=repo_names, y=stars)
fig.show()