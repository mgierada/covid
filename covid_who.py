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
    def __init__(self):
        self.link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
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

    def new_cases_to_death(self, country):
        country_data = self.analyze(country)
        new_cases = country_data['New_cases']
        new_deaths = country_data['New_deaths']
        # nans = new_case_to_new_deaths_ratio.isna()

        # print(new_case_to_new_deaths_ratio)
        country_data['New_cases_to_new_deaths_ratio'] = new_cases/new_deaths
        country_data['New_cases_to_new_deaths_ratio'].interpolate(
            method='linear', axis=0, inplace=True)
        country_data['New_cases_to_new_deaths_ratio'].plot(
            title='New cases to new death ratio')
        plt.show()

    def new_death_to_cumultative_deaths(self, country):
        country_data = self.analyze(country)
        cumulative_deaths = country_data['Cumulative_deaths']
        new_deaths = country_data['New_deaths']
        country_data['New_deaths_to_cumulative_deaths'] = new_deaths / \
            cumulative_deaths
        country_data['New_deaths_to_cumulative_deaths'].plot(
            title='New deaths to cumulative deaths')
        plt.show()

    def get_country_with_max_new_cases(self, date):
        data = self.load_data()
        mask = data.loc[:, 'Date_reported'] == date
        date_data = data[mask]
        max_value_idx = date_data['New_cases'].argmax()
        max_new_cases = date_data['New_cases'].max()
        max_new_cases_country_data = date_data.iloc[max_value_idx]
        country = max_new_cases_country_data['Country']
        return country, max_new_cases

    def get_country_with_max_new_deaths(self, date):
        data = self.load_data()
        mask = data.loc[:, 'Date_reported'] == date
        date_data = data[mask]
        max_value_idx = date_data['New_deaths'].argmax()
        max_new_deaths = date_data['New_deaths'].max()
        max_new_deaths_country_data = date_data.iloc[max_value_idx]
        country = max_new_deaths_country_data['Country']
        return country, max_new_deaths

    def overview(self, date):
        country_max_new_cases, max_new_cases = self.get_country_with_max_new_cases(
            date)
        country_max_new_deaths, max_new_deaths = self.get_country_with_max_new_deaths(
            date)
        print('Country with the most new cases reported for {}:'.format(date))
        print('==============================================================')
        print('    {}'.format(country_max_new_cases))
        print('    {} new cases'.format(max_new_cases))
        print('Country with the most new deaths reported for {}:'.format(date))
        print('==============================================================')
        print('    {}'.format(country_max_new_deaths))
        print('    {} new deaths'.format(max_new_deaths))

    def plot(self, countries):
        _, axes = plt.subplots(2, 2)
        # plt.figure(figsize=(20, 20))
        for num, country in enumerate(countries):
            selected_country = self.analyze(country)
            selected_country.plot(ax=axes[num][0], logy=True, title=country)
            selected_country['New_cases'].plot(ax=axes[num][1])
        plt.tight_layout()
        plt.gcf().set_size_inches(10, 10)
        plt.savefig('plot.png')
        # plt.show()

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
        print(a, b)
        y = np.exp(b) * np.exp(a*days)
        plt.plot(days, new, "o")
        plt.plot(days, y)
        plt.show()

        # new_cases.plot()
        # plt.show()


# countries = ['Poland', 'United States of America']
countries = ['United States of America']
# Covid_WHO().get_data()
# Covid_WHO().plot(countries)
# Covid_WHO(link).predict('Poland')
# Covid_WHO().new_death_to_cumultative_deaths('Poland')
Covid_WHO().overview('2020-12-13')
