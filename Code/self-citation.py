import pandas as pd
import numpy as np


def self_citation():
    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    Top15['ratio'] = Top15['Self-citations'] / Top15['Citations']
    index = Top15[Top15['ratio'] == np.max(Top15['ratio'])].index[0]
    answer = (Top15['Country'].iloc[index], Top15['ratio'].iloc[index])
    return answer

print(self_citation())