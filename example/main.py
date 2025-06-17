from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="{{secrets.chains_firecrawl}}")

scrape_status = app.scrape_url(params['website_url'])

return scrape_status