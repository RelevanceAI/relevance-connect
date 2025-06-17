# RELEVANCE CONNECT
Open connector to add integrations to Relevance AI.

## Create a new integration
1. Install the Relevance Connect CLI: `pip install relevance_connect`
2. Create a folder for the integration.
3. Create a single `metadata.json` file. This is a JSON file that contains the metadata for the integration.
```json
{
    "name": "Firecrawl", // Name of the integration
    "description": "Firecrawl is a tool that allows  you to run firecrawl.", // Description of the integration
    "inputs": [
        {
            "input_name": "website_url",
            "type": "string",
            "title": "Website URL",
            "description": "The URL of the website to crawl.",
            "default": "https://www.firecrawl.dev",
            "required": true
        },
        {
            "input_name": "firecrawl",
            "type": "string",
            "title": "Firecrawl API Key",
            "description": "The API key for firecrawl.",
            "required": true
        }
    ], // Inputs of the integration
    "requirements": ["firecrawl"], // Optional: Requirements of the integration
    "long_output_mode": true, // Optional: If your code returns a long output, greater than 10 million characters, set this to true.
    "timeout": 300 // Optional: Timeout of the integration in seconds. Default is 300 seconds.
}
```
4. Create a `main.py` file. This has to be a single file.
- It requires a return statement at the end of the file.
- You can refer to any of the inputs created in the `inputs.py` file via accessing the `params` dictionary. e.g. `params["website_url"]`
- Any api key inputs are stored in a naming convention of `{{secrets.chains_XXX}}` so e.g. `{{secrets.chains_firecrawl}}`
```python
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="{{secrets.chains_firecrawl}}")

scrape_status = app.scrape_url(params['website_url'])

return scrape_status
```
5. Test it:
- create a `inputs.json` file. This is a JSON file that contains the inputs for the integration.
```json
{
    "firecrawl": "firecrawl"
}
```
- run `relevance_connect main.py metadata.json --inputs inputs.json` in the folder of the integration.
6. Submit it!