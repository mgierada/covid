# covidpy

A python package to analyze the Covid-19 cases worldwide.

It's a prototype version that in the future will also include predicting evolution of the disease by implementing a machine learning algorithms.

It automatically gets the dataset from the [https://covid19.who.int/WHO-COVID-19-global-data.csv](WHO) website and ['https://www.worldometers.info/coronavirus/'](worldometer).

By running:

```python
countries = ['Poland', 'United States of America']
Covid_WHO().plot(countries)
```

You will get:

<img src=./plot.png></img>
