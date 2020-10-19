import os
import pandas as pd
import matplotlib.pyplot as plt
from urllib import request


class Covid_WHO():
    def __init__(self, link):
        self.link = link
        self.data_file = os.path.join(os.getcwd(), 'covid_dataset.csv')

    def get_data(self):
        ''' Download the latest Covid dateset from WHO website '''
        request.urlretrieve(self.link, self.data_file)

    def load_data(self):
        data = pd.read_csv(self.data_file)
        data.columns = [col.strip() for col in data.columns]
        data.index = pd.to_datetime(data['Date_reported'])
        return data

    def analyze(self, country):
        data = self.load_data()
        mask = data.loc[:, 'Country'] == country
        selected_country = data[mask]
        return selected_country

    def plot(self, countries):
        _, axes = plt.subplots(2, 2)
        countries = ['Poland', 'United States of America']
        for num, country in enumerate(countries):
            selected_country = self.analyze(country)
            selected_country.plot(ax=axes[num][0], logy=True, title=country)
            selected_country['New_cases'].plot(ax=axes[num][1])
        plt.tight_layout()
        plt.show()


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
countries = ['Poland', 'United States of America']

Covid_WHO(link).plot(countries)
