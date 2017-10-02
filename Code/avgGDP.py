
import pandas as pd
import numpy as np

"""Get the average of GDP in the past 10 years for Top 15 countries"""


def get_avgGDP():
    Top15 = (pd.read_csv("../Data/cleaned_data.csv")
           .set_index('Country'))
    cols = Top15.loc[:, '2006':'2015'].columns
    avgGDP = (Top15.apply(lambda x: np.mean(x[cols]), axis=1)
                   .sort_values(ascending=False))
    avgGDP.name = 'avgGDP'
    return avgGDP

"""Changes in GDP in the past x years of the ith country i in GDP"""


def gap_GDP(i,year):
    Top15 = (pd.read_csv("../Data/cleaned_data.csv")
           .set_index('Country'))
    country = get_avgGDP().index[i]  # sorted top15 by average GDP, take the 6th
    return Top15['2015'].loc[country] - Top15[str(2015-year)].loc[country]


"""Testing"""

# test
print(get_avgGDP())
print(gap_GDP(i=1, year=3))
