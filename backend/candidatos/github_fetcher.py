import requests

def search_candidates_by_location(local='Brazil', per_page=30, page=1):
    url = "https://api.github.com/search/users"
    params = {
        "q": f"location:{local}",
        "per_page": per_page,
        "page": page
    }
    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data.get("items", [])
