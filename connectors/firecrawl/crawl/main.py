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

def crawl(payload):
    endpoint = f"{base_url}/crawl"
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
    "url": params["url"]
}

# Add optional parameters if provided
if params.get("exclude_paths"):
    payload['excludePaths'] = params.get("exclude_paths", None)

if params.get("include_paths"):
    payload['includePaths'] = params.get("include_paths", None)

if params.get("max_depth"):
    payload['maxDepth'] = params.get("max_depth", 5)

if params.get("max_discovery_depth"):
    payload['maxDiscoveryDepth'] = params.get("max_discovery_depth", 10)

if params.get("ignore_sitemap"):
    payload['ignoreSitemap'] = params.get("ignore_sitemap", False)

if params.get("ignore_query_parameters"):
    payload['ignoreQueryParameters'] = params.get("ignore_query_parameters", False)

if params.get("limit"):
    payload['limit'] = params.get("limit", 10)

if params.get("allow_backward_links"):
    payload['allowBackwardLinks'] = params.get("allow_backward_links", False)

if params.get("allow_external_links"):
    payload['allowExternalLinks'] = params.get("allow_external_links", False)

if params.get("delay"):
    payload['delay'] = params.get("delay", 1000)

if params.get("webhook"):
    payload['webhook'] = params.get("webhook", None)

if params.get("scrape_options"):
    payload['scrapeOptions'] = params.get("scrape_options", None)

# Make the request
return crawl(payload)