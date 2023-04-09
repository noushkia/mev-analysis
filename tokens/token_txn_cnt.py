import requests
import pandas as pd
import re
from datetime import datetime

API_KEY = "2EKdnJxVDhsvMSQUCs6oOQjUd6O"


def get_txn_cnt(symbol: str = 'ETH') -> int:
    response = requests.get(url="https://api.glassnode.com/v1/metrics/transactions/count",
                            params={'api_key': API_KEY, 'a': symbol, })

    counts_tup = response.text.strip('[').strip(']').split('},{')
    counts_tup[0] = counts_tup[0].strip('{')
    counts = [re.findall(r"\d*\.\d+|\d+", row) for row in counts_tup]
    counts_df = pd.DataFrame(counts, columns=['time', 'txn cnt'])
    counts_df['time'] = counts_df['time'].apply(lambda t: datetime.fromtimestamp(int(t)).date())
    counts_df['txn cnt'] = counts_df['txn cnt'].astype(float)

    return counts_df['txn cnt'].sum()


symbols = ['ETH']
symbols_cnt = {}

for symbol in symbols:
    symbols_cnt[symbol] = get_txn_cnt(symbol=symbol)
