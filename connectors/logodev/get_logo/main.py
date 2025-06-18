import requests

# Get the API key from secrets
api_key = "{{secrets.chains_logodev}}"

# Get the domain from parameters
domain = params['domain']

# Build the URL
url = f"https://img.logo.dev/{domain}"

# Build query parameters
query_params = {
    "token": api_key
}

# Add optional parameters if provided
if params.get('size'):
    query_params['size'] = params['size']

if params.get('format'):
    query_params['format'] = params['format']

if params.get('greyscale'):
    query_params['greyscale'] = str(params['greyscale']).lower()

if params.get('fallback'):
    query_params['fallback'] = params['fallback']

if params.get('retina'):
    query_params['retina'] = str(params['retina']).lower()

# Make the request
response = requests.get(url, params=query_params)

# Check if the request was successful
if response.status_code == 200:
    # Return the image URL with all parameters
    return {
        "logo_url": response.url,
        "domain": domain,
        "status": "success",
        "format": params.get('format', 'jpg'),
        "size": params.get('size', 128)
    }
else:
    return {
        "error": f"API request failed with status code {response.status_code}",
        "message": response.text,
        "domain": domain,
        "status": "error"
    }