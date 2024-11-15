import requests

#make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'applicatoin/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
print(response_dict.keys())
print(response_dict['total_count'])
print(response_dict['incomplete_results'])
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
#repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#    print(key)
for repo_dict in repo_dicts:
    print("\nSelected info about the first repository:")
    print(f"name: {repo_dict['name']}")
    print(f"owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")





