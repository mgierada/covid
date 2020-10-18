import os
from urllib import request


def get_data(link):
    data = os.path.join(os.getcwd(), 'covid_dataset.csv')
    request.urlretrieve(link, data)


link = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
get_data(link)
