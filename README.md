# THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY!

Please keep in mind that I do **NOT** encourage breaking any sort of security on websites.

# bingx-headers-generator

BingX Headers Generator is an python library which generates for you all required headers to make requests to BingX API endpoints

# Installation

```
pip install bingx-headers-generator
```

# Examples

```python
from bingx_headers_generator import BingXHeadersGenerator

# btw as I recently checked generator works even with wrong app_version but I left that option in advance of BingX API changes
bingx_headers_generator = BingXHeadersGenerator(
    "4.72.31",
    "1020975128917528579",
    "1052672282142707717",
)

# you can only generate headers
##### AVAILABLE BASE_URLS: #####
# CURRENT POSITIONS FOR STANDARD ACC -> https://bingx.com/api/v1/copy-trade/traderContractHold
# CURRENT POSITIONS FOR PERPETUAL or FUTURES ACC -> https://bingx.com/api/copytrade/v2/real/trader/positions
# TRADE HISTORY -> https://bingx.com/api/v3/trader/orders/v3

headers = bingx_headers_generator.generate_headers("https://bingx.com/api/v3/trader/orders/v3")

```

# How did I find out how to generate headers?

In one of their site files(**https://bin.bb-os.com/_nuxt/1491b29.js**) I found interesting function - `function wt(e)` Go check it and you follow other functions that are called in `wt()` and I'm sure you will start to understand the whole process of generating headers

<img width="1134" alt="Screenshot 2023-04-04 at 23 12 48" src="https://user-images.githubusercontent.com/50675404/229923789-89571a8b-7372-4c1a-9386-6b9ceecd3fe3.png">

