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
