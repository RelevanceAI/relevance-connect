import requests
import json

# Get the API key from secrets
api_key = "{{secrets.chains_exa}}"

# Set up the request
url = "https://api.exa.ai/search"
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Build the request payload
payload = {
    "query": params['query'],
    "numResults": params.get('num_results', 10)
}

# Add optional parameters if provided
if params.get('search_type'):
    payload['type'] = params['search_type']

if params.get('category'):
    payload['category'] = params['category']

if params.get('include_domains'):
    payload['includeDomains'] = params['include_domains']

if params.get('exclude_domains'):
    payload['excludeDomains'] = params['exclude_domains']

if params.get('start_crawl_date'):
    payload['startCrawlDate'] = params['start_crawl_date']

if params.get('end_crawl_date'):
    payload['endCrawlDate'] = params['end_crawl_date']

if params.get('start_published_date'):
    payload['startPublishedDate'] = params['start_published_date']

if params.get('end_published_date'):
    payload['endPublishedDate'] = params['end_published_date']

if params.get('include_text'):
    payload['includeText'] = params['include_text']

if params.get('exclude_text'):
    payload['excludeText'] = params['exclude_text']

# Add contents configuration if requested
if params.get('include_contents'):
    contents_config = {}
    
    if params.get('include_text_content'):
        contents_config['text'] = True
    
    if params.get('include_highlights'):
        contents_config['highlights'] = True
    
    if params.get('include_summary'):
        contents_config['summary'] = True
    
    if contents_config:
        payload['contents'] = contents_config

# Make the request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    return response.json()
else:
    return {
        "error": f"API request failed with status code {response.status_code}",
        "message": response.text
    }