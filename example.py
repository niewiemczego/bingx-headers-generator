from bingx_headers_generator import BingXHeadersGenerator

# custom headers are NOT necessary, but are just an additional option you can pass to request
custom_headers = {
    "cache-control": "no-cache, no-store, must-revalidate",
    "pragma": "no-cache",
    "expires": "0",
}

# btw as I recently checked generator works even with wrong app_version but I left that option in advance of BingX API changes
bingx_headers_generator = BingXHeadersGenerator(
    "4.58.39",
    "1020975128917528579",
    "1052672282142707717",
)

# you can only generate headers
headers = bingx_headers_generator.generate_headers(custom_headers)

# also you can generate just sign header
sign = bingx_headers_generator.generate_sign()

# or you can make full request
res = bingx_headers_generator.make_request(
    "GET",
    "https://api-app.we-api.com/api/copytrade/v1/real/trader/positions",
    custom_headers,
)