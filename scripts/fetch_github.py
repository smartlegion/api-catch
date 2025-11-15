import requests
import json

GITHUB_USERNAME = "smartlegionlab"
EXCLUDED_REPOS = ["smartlegionlab"]

def fetch_github_repos():
    print("🚀 Starting GitHub repositories fetch...")
    
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&per_page=100"
    response = requests.get(url)
    response.raise_for_status()
    
    repos = response.json()
    
    filtered_repos = [
        repo for repo in repos 
        if not repo['archived'] and repo['name'] not in EXCLUDED_REPOS
    ]
    
    sorted_repos = sorted(filtered_repos, key=lambda x: x['pushed_at'], reverse=True)
    
    simplified_repos = []
    for repo in sorted_repos:
        simplified_repos.append({
            'id': repo['id'],
            'name': repo['name'],
            'full_name': repo['full_name'],
            'html_url': repo['html_url'],
            'description': repo['description'],
            'language': repo['language'],
            'stargazers_count': repo['stargazers_count'],
            'forks_count': repo['forks_count'],
            'watchers_count': repo['watchers_count'],
            'topics': repo.get('topics', []),
            'created_at': repo['created_at'],
            'updated_at': repo['updated_at'],
            'pushed_at': repo['pushed_at'],
            'size': repo['size'],
            'archived': repo['archived'],
            'private': repo['private'],
            'fork': repo['fork'],
            'owner': {
                'login': repo['owner']['login'],
                'avatar_url': repo['owner']['avatar_url']
            }
        })
    
    with open('github_repos.json', 'w', encoding='utf-8') as f:
        json.dump(simplified_repos, f, indent=2, ensure_ascii=False)
    
    print(f"✅ SUCCESS: Fetched {len(sorted_repos)} repositories")

if __name__ == "__main__":
    fetch_github_repos()
