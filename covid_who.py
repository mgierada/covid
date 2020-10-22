from math import log
from operator import ne
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from urllib import request
from sklearn.linear_model import LogisticRegression
from scipy.optimize import curve_fit


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
        # plt.figure(figsize=(20, 20))
        for num, country in enumerate(countries):
            selected_country = self.analyze(country)
            selected_country.plot(ax=axes[num][0], logy=True, title=country)
            selected_country['New_cases'].plot(ax=axes[num][1])
        plt.tight_layout()
        plt.gcf().set_size_inches(15, 15)
        plt.show()

    def exponential_fit(self, x, a, b, c):
        return a*np.exp(-b*x) + c

    def predict(self, country):
        # self.get_data()
        data = self.analyze(country)
        new_cases = data['New_cases']
        # new_cases = data['New_cases'].to_string(index=False)
        new = np.array(new_cases)
        new[new == 0] = 1
        days = np.arange(1, len(new_cases) + 1)
        log_new = np.log(new)
        log_days = np.log(days)
        a, b = np.polyfit(days, log_new, 1)
        y = np.exp(b) * np.exp(a*days)
        plt.plot(days, new, "o")
        plt.plot(days, y)
        plt.show()

        # new_cases.plot()
        # plt.show()


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
countries = ['Poland', 'United States of America']

# Covid_WHO(link).plot(countries)
Covid_WHO(link).predict('Poland')
