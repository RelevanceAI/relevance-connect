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

def search(payload):
    endpoint = f"{base_url}/search"
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

# Build the request payload
payload = {
    "query": params['query'],
}

# Add optional parameters if provided
if params.get('limit'):
    payload['limit'] = params['limit']

if params.get('tbs'):
    payload['tbs'] = params['tbs']

if params.get('location'):
    payload['location'] = params['location']

if params.get('timeout'):
    payload['timeout'] = params['timeout']

if params.get('ignore_invalid_urls'):
    payload['ignore_invalid_urls'] = params['ignore_invalid_urls']

if params.get('scrape_options'):
    payload['scrape_options'] = params['scrape_options']

# Make the request
return search(payload)