import requests
from plotly.graph_objs import Bar
from plotly import offline

#make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'applicatoin/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
repo_dicts=response_dict['items']
repo_names, repo_links, stars, labels = [],[],[],[]

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repo_url = repo_dict['html_url']
    repo_links.append(f"<a href='{repo_url}'>{repo_dict['name']}")
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

#make visualizations
data = [{
    'type': 'bar', 
    'x': repo_links, 
    'y': stars, 
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},    
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},   
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')