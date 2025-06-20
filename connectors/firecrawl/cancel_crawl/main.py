import requests
import json

# Get the API key from secrets
api_key = "{{secrets.chains_firecrawl}}"

base_url = "https://api.firecrawl.dev/v1"
base_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def cancel_crawl(crawl_id):
    endpoint = f"{base_url}/crawl/{crawl_id}"
    response = requests.delete(endpoint, headers=base_headers)
    return handle_response(response)

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"API request failed with status code {response.status_code}",
            "message": response.text
        }

# Make the request
return cancel_crawl(params["crawl_id"])