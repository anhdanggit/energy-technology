import pandas as pd


def pop_rank(i):

    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Pop = Top15['Population'].sort_values(ascending=False).iloc[i-1]  # take the ith most populous
    Country = Top15[Top15['Population'] == Pop]['Country'].iloc[0]
    answer = (Country)
    return answer

print(pop_rank(3))

'''Convert the Population Estimate series to a string with thousands separator (using commas). 
Do not round the results.'''

def print_pop():
    import pandas as pd

    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    def forstring(x):
        return '{:,}'.format(x)
    return Top15['PopEst'].map(forstring)

print(print_pop())