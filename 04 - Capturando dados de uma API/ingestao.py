from abc import ABC, abstractmethod
import requests
import logging
import datetime

# o __name__ se refere ao nome do arquivo, o nome do logger será esse.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MercadoBitcoinApi(ABC):

    def __init__(self, coin):
        self.coin = coin
        self.base_endpoint = 'https://www.mercadobitcoin.net/api'

    @abstractmethod
    def _get_endpoint(self, **kwargs):
        pass

    def get_data(self, **kwargs):
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f'Getting data from endpoint: {endpoint}')
        response = requests.get(endpoint)
        response.raise_for_status()

        return response.json()


class DaySummaryApi(MercadoBitcoinApi):
    type = 'day-summary'

    def _get_endpoint(self, date: datetime.date):
        return f'{self.base_endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}'


# print(DaySummaryApi(coin='BTC').get_data(date=datetime.date(2022, 11, 1)))


class TradesAPI(MercadoBitcoinApi):
    type = 'trades'

    def get_unix_epoch(self, date: datetime.datetime):
        return int(date.timestamp())

    def _get_endpoint(self, date_from: datetime.datetime = None, date_to: datetime.datetime = None):
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


print(TradesAPI(coin='BTC').get_data())
print(TradesAPI(coin='BTC').get_data(date_from=datetime.datetime(2022, 11, 1)))
print(TradesAPI(coin='BTC').get_data(date_from=datetime.datetime(2022, 10, 1), date_to=datetime.datetime(2022, 10, 10)))
