import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import requests


class Covid_Worldsometer:
    def __init__(self, url):
        self.url = url
        self.data_file = os.path.join(
            os.getcwd(), 'covid_dataset_worldometer.csv')

    def get_data(self):
        html_source = requests.get(self.url).text
        html_source = re.sub(
            r'<.*?>', lambda g: g.group(0).upper(), html_source)
        data = pd.read_html(html_source, header=[0], index_col=0, skiprows=range(1, 10))[
            0].iloc[:-1]
        data.rename(columns={'Country,Other': 'Country'}, inplace=True)
        data.to_csv(self.data_file)

    def analyze(self, country):
        data = self.get_data()
        mask = data['Country'] == country
        country = data[mask]
        return country


url = 'https://www.worldometers.info/coronavirus/'
Covid_Worldsometer(url).get_data()
