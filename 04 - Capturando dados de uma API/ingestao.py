# url = 'https://www.mercadobitcoin.net/api/BTC/day-summary/2022/11/01'
# response = requests.get(url)
# print(response.raise_for_status())
# print(response.json())
import datetime

import requests
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# Classe para lidar com as requisições

class MercadoBitcoinApi(ABC):

    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.base_endpoint = 'https://www.mercadobitcoin.net/api'

    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f'Getting data from endpoint: {endpoint}')
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


# print(MercadoBitcoinApi(coin='BTC').get_data())
# print(MercadoBitcoinApi(coin='LTC').get_data())

# cria a class para extrair o Day Summary
class DaySummaryApi(MercadoBitcoinApi):
    type = "day-summary"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f'{self.base_endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}'


# print(DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 10, 4)))

# cria a class para extrair os Traders
class TradesApi(MercadoBitcoinApi):
    type = "trades"

    def get_unix_epoch(self, date: datetime.datetime) -> int:
        return int(date.timestamp())

    def _get_endpoint(self, date_from: datetime.datetime = None, date_to: datetime.datetime = None) -> str:

        if date_from and not date_to:
            unix_date_from = self.get_unix_epoch(date_from)
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}/{unix_date_from}'

        elif date_from and date_to:
            unix_date_from = self.get_unix_epoch(date_from)
            unix_date_to = self.get_unix_epoch(date_to)
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}/{unix_date_from}/{unix_date_to}'

        else:
            endpoint = f'{self.base_endpoint}/{self.coin}/{self.type}'

        return endpoint


print(TradesApi(coin='BTC').get_data())
print(TradesApi(coin='BTC').get_data(date_from=datetime.datetime(2022, 10, 1)))
print(TradesApi(coin='BTC').get_data(date_from=datetime.datetime(2022, 10, 2), date_to=datetime.datetime(2022, 10, 3)))
