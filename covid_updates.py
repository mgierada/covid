import os
import pandas as pd
from urllib import request


class Covid():
    def __init__(self, link):
        self.link = link
        self.data_file = os.path.join(os.getcwd(), 'covid_dataset.csv')

    def get_data(self):
        ''' Download the latest Covid dateset from WHO website '''
        request.urlretrieve(self.link, self.data_file)

    def load_data(self):
        data = pd.read_csv(self.data_file)
        data.columns = [col.strip() for col in data.columns]
        print(data.Country)
        return data

    def analyze(self, country):
        data = self.load_data()
        # print(data)


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

Covid(link).analyze('Poland')
