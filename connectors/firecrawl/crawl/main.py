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


def crawl(params):
    url = params.get("url")
    exclude_paths = params.get("exclude_paths", None)
    include_paths = params.get("include_paths", None)
    max_depth = params.get("max_depth", 5)
    max_discovery_depth = params.get("max_discovery_depth", 10)
    ignore_sitemap = params.get("ignore_sitemap", False)
    ignore_query_parameters = params.get("ignore_query_parameters", False)
    limit = params.get("limit", 10)
    allow_backward_links = params.get("allow_backward_links", False)
    allow_external_links = params.get("allow_external_links", False)
    delay = params.get("delay", 1000)
    webhook = params.get("webhook", None)
    scrape_options = params.get("scrape_options", None)

    endpoint = f"{base_url}/crawl"
    payload = {
        "url": url,
        "excludePaths": exclude_paths,
        "includePaths": include_paths,
        "maxDepth": max_depth,
        "maxDiscoveryDepth": max_discovery_depth,
        "ignoreSitemap": ignore_sitemap,
        "ignoreQueryParameters": ignore_query_parameters,
        "limit": limit,
        "allowBackwardLinks": allow_backward_links,
        "allowExternalLinks": allow_external_links,
        "delay": delay,
        "webhook": webhook,
        "scrapeOptions": scrape_options
    }
    payload = remove_none_values(payload)
    response = requests.post(endpoint, headers=base_headers, json=payload)
    return handle_response(response)

def get_crawl_status(crawl_id):
    endpoint = f"{base_url}/crawl/{crawl_id}"
    response = requests.get(endpoint, headers=base_headers)
    return handle_response(response)

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