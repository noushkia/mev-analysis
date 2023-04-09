import sys
import traceback

import requests
import pandas as pd
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# dataframe that stores the name tags
name_tag_df = pd.read_csv("tokens.csv", names=['address', 'tag'], index_col='address')

# header required for the GET request
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/96.0.4664.110 Safari/537.36'}


def get_name_tag(_address: str) -> str:
    """
    gets the public name tag assigned to the address by etherscan.
    if the address was never added to the list, it'll find the name
    using request.get and add the new pair to the list.
    """
    if _address in name_tag_df.index:
        logging.info(f"Already found: {name_tag_df.loc[_address].tag}")
        return name_tag_df.loc[_address].tag
    else:
        logging.info(f"Finding {_address}")

        url = f"https://etherscan.io/address/{_address}"

        response = requests.get(url=url, headers=headers)

        try:
            new_tag = response.text.split('<')[4].split('|')[0].split('\t')[1].strip()

            name_tag_df.loc[_address] = new_tag

            logging.info(f"Found {new_tag}")
            name_tag_df.to_csv('tokens.csv', header=False)
            response.close()
            return new_tag

        except IndexError as err:
            logging.error(f"Error: {err}")
            print(response.text)
            traceback.print_exc()

        return "Not Found"


if __name__ == "__main__":
    with open('addresses.txt', 'r') as f:
        for address in f.readlines():
            get_name_tag(address.strip('\n'))
