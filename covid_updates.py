import os
from urllib import request


class Covid():
    def __init__(self, link):
        self.link = link

    def get_data(self):
        data = os.path.join(os.getcwd(), 'covid_dataset.csv')
        request.urlretrieve(self.link, data)


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

Covid(link).get_data()
