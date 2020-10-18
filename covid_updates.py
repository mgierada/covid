import os
import pandas as pd
import matplotlib.pyplot as plt
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
        # data['Date_reported'] = pd.to_datetime[data['Date_reported']]
        data.index = pd.to_datetime(data['Date_reported'])
        return data

    def analyze(self, country):
        data = self.load_data()
        mask = data.loc[:, 'Country'] == country
        selected_country = data[mask]
        total_cases = selected_country['Cumulative_cases']
        day_reported = selected_country['Date_reported']
        selected_country.plot()
        # plt.plot(day_reported, total_cases)
        plt.show()


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

Covid(link).analyze('Poland')
