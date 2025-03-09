import requests


class RequestCollector:
    def __init__(self):
        self.url = r'http://26.241.32.104:5001/'

    def get_date_data(self, date_key):
        day, month, year = date_key.split('-')
        return requests.get(f'{self.url}?day={day}&month={month}&year={year}').json()['message']

    def get_dates_data(self):
        dates_keys = requests.get(self.url + 'date').json()['message']

        return [(date_key, self.get_date_data(date_key)) for date_key in dates_keys]

    def test_algo(self, date_key, algorithm_result):
        data = {
            "data": {
                "count": len(algorithm_result),
                "rooms": algorithm_result
            },
            "date": date_key
        }

        return requests.post(self.url, json=data).json()['message']


if __name__ == '__main__':
    rc = RequestCollector()
    print(rc.get_dates_data())
