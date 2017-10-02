
import numpy as np
import pandas as pd

"""Find the Average of a specific col"""


def mean_col(col):
    Top15 = (pd.read_csv("../Data/cleaned_data.csv")
           .set_index('Country'))
    return np.mean(Top15[col])

#test
print(mean_col(col='Energy Supply per Capita'))

"""Find a maximum of a variable and its countries"""


def find_max(col):
    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    index = Top15[Top15[col] == np.max(Top15[col])].index[0]
    answer = (Top15['Country'].iloc[index], Top15[col].iloc[index])
    return answer

#test
print(find_max('% Renewable'))
