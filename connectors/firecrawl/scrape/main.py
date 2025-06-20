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


def scrape(params):
    url = params.get("url")
    formats = params.get("formats", ["markdown"])
    only_main_content = params.get("only_main_content", True)
    include_tags = params.get("include_tags", None)
    exclude_tags = params.get("exclude_tags", None)
    max_age = params.get("max_age", 0)
    headers = params.get("headers", None)
    wait_for = params.get("wait_for", 0)
    mobile = params.get("mobile", False)
    skip_tls_verification = params.get("skip_tls_verification", False)
    timeout = params.get("timeout", 30000)
    parse_pdf = params.get("parse_pdf", True)
    json_options = params.get("json_options", None)
    actions = params.get("actions", None)
    location = params.get("location", None)
    remove_base64_images = params.get("remove_base64_images", True)
    block_ads = params.get("block_ads", True)
    proxy = params.get("proxy", "basic")
    change_tracking_options = params.get("change_tracking_options", None)
    store_in_cache = params.get("store_in_cache", True)

    endpoint = f"{base_url}/scrape"
    payload = {
        "url": url,
        "formats": formats,
        "onlyMainContent": only_main_content,
        "includeTags": include_tags,
        "excludeTags": exclude_tags,
        "maxAge": max_age,
        "headers": headers,
        "waitFor": wait_for,
        "mobile": mobile,
        "skipTlsVerification": skip_tls_verification,
        "timeout": timeout,
        "parsePDF": parse_pdf,
        "jsonOptions": json_options,
        "actions": actions,
        "location": location,
        "removeBase64Images": remove_base64_images,
        "blockAds": block_ads,
        "proxy": proxy,
        "changeTrackingOptions": change_tracking_options,
        "storeInCache": store_in_cache
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
