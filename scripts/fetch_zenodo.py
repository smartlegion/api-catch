import requests
import json

ZENODO_RECORDS = {
    'pointerParadigm': '17204738',
    'localDataParadigm': '17264327', 
    'deterministicEngine': '17383447'
}

def fetch_zenodo_stats(record_id):
    try:
        response = requests.get(f"https://zenodo.org/api/records/{record_id}", timeout=10)
        response.raise_for_status()
        
        data = response.json()
        stats = data.get('stats', {})
        
        return {
            'unique_views': stats.get('unique_views', 0),
            'unique_downloads': stats.get('unique_downloads', 0), 
            'total_views': stats.get('views', 0),
            'total_downloads': stats.get('downloads', 0)
        }
    except Exception as e:
        print(f"⚠️ Error fetching {record_id}: {e}")
        return {
            'unique_views': 0,
            'unique_downloads': 0,
            'total_views': 0, 
            'total_downloads': 0
        }

def fetch_all_zenodo_stats():
    print("🚀 Starting Zenodo statistics fetch...")
    
    stats = {}
    for name, record_id in ZENODO_RECORDS.items():
        stats[name] = fetch_zenodo_stats(record_id)
    
    with open('zenodo_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print("✅ SUCCESS: Fetched all Zenodo statistics")

if __name__ == "__main__":
    fetch_all_zenodo_stats()
