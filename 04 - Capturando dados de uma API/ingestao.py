import requests


class MercadoBitcoinApi():

    def __init__(self, coin):
        self.coin = coin
        self.base_endpoint = 'https://www.mercadobitcoin.net/api'

    def _get_endpoint(self):
        return f"{self.base_endpoint}/{self.coin}/day-summary/2022/11/29"

    def get_data(self):
        endpoint = self._get_endpoint()
        response = requests.get(endpoint)
        return response.json()


print(MercadoBitcoinApi(coin='BTC').get_data())
