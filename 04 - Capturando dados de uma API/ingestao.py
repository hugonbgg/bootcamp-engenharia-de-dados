# url = 'https://www.mercadobitcoin.net/api/BTC/day-summary/2022/11/01'
# response = requests.get(url)
# print(response.raise_for_status())
# print(response.json())

import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# Classe para lidar com as requisições

class MercadoBitcoinApi():

    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.base_endpoint = 'https://www.mercadobitcoin.net/api'

    def _get_endpoint(self) -> str:
        return f'{self.base_endpoint}/{self.coin}/day-summary/2022/11/01'

    def get_data(self) -> dict:
        endpoint = self._get_endpoint()
        logger.info(f'Getting data from endpoint: {endpoint}')
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


print(MercadoBitcoinApi(coin='BTC').get_data())
print(MercadoBitcoinApi(coin='LTC').get_data())