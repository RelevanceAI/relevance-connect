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

def map(payload):
    endpoint = f"{base_url}/map"
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
    "url": params['url'],
}

# Add optional parameters if provided
if params.get('search'):
    payload['search'] = params.get('search', None)

if params.get('ignore_sitemap'):
    payload['ignoreSitemap'] = params.get('ignore_sitemap', True)

if params.get('sitemap_only'):
    payload['sitemapOnly'] = params.get('sitemap_only', False)

if params.get('include_subdomains'):
    payload['includeSubdomains'] = params.get('include_subdomains', False)

if params.get('limit'):
    payload['limit'] = params.get('limit', 5000)

if params.get('timeout'):
    payload['timeout'] = params.get('timeout', 10000)

# Make the request
return map(payload)