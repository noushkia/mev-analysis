# Tokens Package
This package gathers all the data required for advanced analysis of arbitrage transactions


## Name Tag
Used for better understanding of addresses.<br>
Maps Ethereum addresses to their assigned etherscan name tag.


## Token Price
Used for evaluating price volatility at the time of arbitrage transactions.<br>
Also used for calculating total profit in USD for a transaction.

## Token Symbol
Used for mapping token addresses to their respective symbols.<br>
This is required for API calls since some APIs require token symbol instead of address.

## Protocol Transaction
Used for normalizing the most used protocols evaluation.<br>
Get the total number of transactions using the input protocol 
and the total number of arbitrage transactions.<br>
Compare the protocols by first normalizing their transaction count.

## Token Transaction
Used for normalizing the most used tokens evaluation.<br>
Get the total number of transactions using the input token 
and the total number of arbitrage transactions.<br>
Compare the tokens by first normalizing their transaction count.

## Address Transaction
Used for comparing total transactions to arbitrage 
transactions executed by an address.
<br>
This might be helpful:
    https://docs.alchemy.com/docs/how-to-get-transaction-history-for-an-address-on-ethereum


## Gas
Possible sign of an arbitrage transaction is a jump in gas price.<br>
Because of PGAs and the competition between arbitrage bots,
the gas price tends to be higher than the normal price.<br>
Yet there are some arbitrages that don't pay much gas, the reason
(strategy) is yet to be discovered.


## APIs
Currently, using Glassnode API:
    https://docs.glassnode.com/

Possible APIs and tools:
CoinMarketCap: https://coinmarketcap.com/api/documentation/v1/ <br>
CoinGecko: https://www.coingecko.com/en/api <br>
Historic-Crypto: https://pypi.org/project/Historic-Crypto/ <br>

Read https://medium.com/geekculture/3-simple-ways-to-obtain-cryptocurrency-data-in-python-f45b9d603a97


____


# Some issues with the current mev-inspector

## Lazy token analysis
The arbitrage model simply calculates profit made by only a single token.<br>
This might not be always true since an arbitrageur can 
hold part of the exchanged token to themselves due to price impact
making total profit made by two tokens.<br>


## Lack of Useful Features
Must gather more features for each arbitrage transaction<br>
Proposed features:<br>
    Address txn history(?)<br>
    Transaction type(?)<br>

