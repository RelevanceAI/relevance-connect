import requests
import json

# Get the API key from secrets
api_key = "{{secrets.chains_firecrawl}}"

base_url = "https://api.firecrawl.dev/v1"
base_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def remove_none_values(payload):
    return {k: v for k, v in payload.items() if v is not None}


def map(params):
    url = params.get("url")
    search = params.get("search", None)
    ignore_sitemap = params.get("ignore_sitemap", True)
    sitemap_only = params.get("sitemap_only", False)
    include_subdomains = params.get("include_subdomains", False)
    limit = params.get("limit", 5000)
    timeout = params.get("timeout", 10000)

    endpoint = f"{base_url}/map"
    payload = {
        "url": url,
        "search": search,
        "ignoreSitemap": ignore_sitemap,
        "sitemapOnly": sitemap_only,
        "includeSubdomains": include_subdomains,
        "limit": limit,
        "timeout": timeout
    }
    payload = remove_none_values(payload)
    response = requests.post(endpoint, headers=base_headers, json=payload)
    return handle_response(response)


def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"API request failed with status code {response.status_code}",
            "message": response.text
        } 