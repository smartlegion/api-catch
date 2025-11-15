import requests
import json

def fetch_devto_articles():
    print("🚀 Starting Dev.to articles fetch...")
    
    url = "https://dev.to/api/articles?username=smartlegionlab&per_page=100"
    response = requests.get(url)
    response.raise_for_status()
    
    articles = response.json()
    
    with open('devto_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    
    print(f"✅ SUCCESS: Fetched {len(articles)} articles")

if __name__ == "__main__":
    fetch_devto_articles()
