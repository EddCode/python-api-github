import requests
from plotly.graph_objs import Bar
from plotly import offline


def get_repos_list(language):
    url = f'https://api.github.com/search/repositories?q=language:{language.lower()}&sort=stars'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)

    response = r.json()

    repos_name, repos_star, labels = [], [] , []

    for repo_dict in response['items']:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f'<a href="{repo_url}">{repo_name}</a>'

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner} -- {description}"
        labels.append(label)

        repos_name.append(repo_link)
        repos_star.append(repo_dict['stargazers_count'])


    print(f"Total repositories: {response['total_count']}")
    print(f"Status code: {r.status_code}")

    data_visualization = [{
        'type': 'git_repos',
        'x': repos_name,
        'y': repos_star,
        'overtext': labels,
        'marker': {
            'color': 'rgb(255, 0, 0)',
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 1.5,
            }
        },
        'opacity': 0.9,
    }]

    layout = {
        'title': f'Top 5 most starred {language.title()} repositories on Github',
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

    fig = {'data': data_visualization, 'layout': layout}

    return fig


if __name__ == '__main__':
    language = input("Enter a GitHub language repository: ")

    fig = get_repos_list(language)
    #offline.plot(fig, filename=f'{language}_info.html')

