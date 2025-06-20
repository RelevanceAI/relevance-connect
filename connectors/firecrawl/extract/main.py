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

def extract(payload):
    endpoint = f"{base_url}/extract"
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
    "urls": params["urls"],
    "prompt": params["prompt"]
}

if params.get("schema"):
    payload["schema"] = params.get("schema", None)

if params.get("enable_web_search"):
    payload["enableWebSearch"] = params.get("enable_web_search", False)

if params.get("ignore_sitemap"):
    payload["ignoreSitemap"] = params.get("ignore_sitemap", False)

if params.get("include_subdomains"):
    payload["includeSubdomains"] = params.get("include_subdomains", True)

if params.get("show_sources"):
    payload["showSources"] = params.get("show_sources", False)

if params.get("scrape_options"):
    payload["scrapeOptions"] = params.get("scrape_options", None)

if params.get("ignore_invalid_urls"):
    payload["ignoreInvalidURLs"] = params.get("ignore_invalid_urls", False)

# Make the request
return extract(payload)