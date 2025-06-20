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


def extract(params):
    urls = params.get("urls")
    prompt = params.get("prompt")
    schema = params.get("schema", None)
    enable_web_search = params.get("enable_web_search", False)
    ignore_sitemap = params.get("ignore_sitemap", False)
    include_subdomains = params.get("include_subdomains", True)
    show_sources = params.get("show_sources", False)
    scrape_options = params.get("scrape_options", None)
    ignore_invalid_urls = params.get("ignore_invalid_urls", False)

    endpoint = f"{base_url}/extract"
    payload = {
        "urls": urls,
        "prompt": prompt,
        "schema": schema,
        "enableWebSearch": enable_web_search,
        "ignoreSitemap": ignore_sitemap,
        "includeSubdomains": include_subdomains,
        "showSources": show_sources,
        "scrapeOptions": scrape_options,
        "ignoreInvalidURLs": ignore_invalid_urls
    }
    payload = remove_none_values(payload)
    response = requests.post(endpoint, headers=base_headers, json=payload)
    return handle_response(response)

def get_extract_status(extract_id):
    endpoint = f"{base_url}/extract/{extract_id}"
    response = requests.get(endpoint, headers=base_headers)
    return handle_response(response)


def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"API request failed with status code {response.status_code}",
            "message": response.text
        } 