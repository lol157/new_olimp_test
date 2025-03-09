import requests


class RequestCollector:
    def __init__(self):
        self.url = r'http://26.241.32.104:5001/'

    def get_date_data(self, date_key):
        day, month, year = date_key.split('-')
        return requests.get(f'{self.url}?day={day}&month={month}&year={year}').json()['message']

    def get_dates_data(self):
        dates = requests.get(self.url + 'date/').json()['message']

        return [self.get_date_data(date) for date in dates]


if __name__ == '__main__':
    rc = RequestCollector()
    print(rc.get_dates_data())



