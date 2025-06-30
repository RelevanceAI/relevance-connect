import requests

# Get the API key from secrets
api_key = "{{secrets.chains_parallel}}"

base_url = "https://api.parallel.ai/alpha/search"
base_headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

def search(payload):
    response = requests.post(base_url, json=payload, headers=base_headers)
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
    "objective": params["objective"],
    "search_queries": params["search_queries"],
    "processor": params.get("processor", "base"),
    "max_results": params.get("max_results", 5),
    "max_chars_per_result": params.get("max_chars_per_result", 1500)
}

# Make the request
return search(payload)
