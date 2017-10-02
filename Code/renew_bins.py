
'''Count countries by continent level and set bins of % Renewable energy'''

def renew_bin(n):

    import pandas as pd

    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    Top15['Continent'] = Top15['Country'].replace(ContinentDict)
    Top15['bin'] = pd.cut(Top15['% Renewable'],n)
    return Top15.groupby(['Continent', 'bin']).size().dropna()

print(renew_bin(n=3))