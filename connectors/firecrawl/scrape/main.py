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

def scrape(payload):
    endpoint = f"{base_url}/scrape"
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
    "url": params["url"],
    "formats": params.get("formats", ["markdown"])
}

# Add optional parameters if provided
if params.get("only_main_content"):
    payload['onlyMainContent'] = params.get("only_main_content", True)

if params.get("include_tags"):
    payload['includeTags'] = params["include_tags"]

if params.get("exclude_tags"):
    payload['excludeTags'] = params["exclude_tags"]

if params.get("max_age"):
    payload['maxAge'] = params.get("max_age", 0)

if params.get("headers"):
    payload['headers'] = params["headers"]

if params.get("wait_for"):
    payload['waitFor'] = params.get("wait_for", 0)

if params.get("mobile"):
    payload['mobile'] = params.get("mobile", False)

if params.get("skip_tls_verification"):
    payload['skipTlsVerification'] = params.get("skip_tls_verification", False)

if params.get("timeout"):
    payload['timeout'] = params.get("timeout", 30000)

if params.get("parse_pdf"):
    payload['parsePDF'] = params.get("parse_pdf", True)

if params.get("json_options"):
    payload['jsonOptions'] = params["json_options"]

if params.get("actions"):
    payload['actions'] = params["actions"]

if params.get("location"):
    payload['location'] = params["location"]

if params.get("remove_base64_images"):
    payload['removeBase64Images'] = params.get("remove_base64_images", True)

if params.get("block_ads"):
    payload['blockAds'] = params.get("block_ads", True)

if params.get("proxy"):
    payload['proxy'] = params.get("proxy", "basic")

if params.get("change_tracking_options"):
    payload['changeTrackingOptions'] = params.get("change_tracking_options", None)

if params.get("store_in_cache"):
    payload['storeInCache'] = params.get("store_in_cache", True)

# Make the request
return scrape(payload)