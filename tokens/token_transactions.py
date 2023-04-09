import requests

API_KEY = "2EIWJ6NIX2PBZ2E43W2R9CHY1JUCUJAX4S"

address = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"


def get_token_txns(start_block: int, end_block: int, token_address: str):
    url = f"http://api.etherscan.io/api?module=account&action=tokentx&address={token_address}" \
          f"&startblock={start_block}&endblock={end_block}&sort=asc&apikey={API_KEY}"

    return requests.get(url=url)
