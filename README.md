# bingx-headers-generator

BingX Headers Generator is an python library which generates for you all required headers to make requests to BingX non-public API endpoints

# Installation

```
pip install bingx-headers-generator
```

# Examples

```python
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

```

# How did I find out how to generate headers?

In one of their site files(**https://bin.bb-os.com/_nuxt/1491b29.js**) I found interesting function - `function wt(e)` Go check it and you follow other functions that are called in `wt()` and I'm sure you will start to understand the whole process of generating headers

# THIS PROJECT IS ONLY FOR LEARN PURPOSE!

Please keep in mind that I do **NOT** encourage breaking any sort of security on websites
