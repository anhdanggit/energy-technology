
'''Summary certain variable by continent level'''

def continent(col):

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
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Continent'] = Top15['Country'].replace(ContinentDict)
    df = Top15.groupby('Continent')[col].agg(['size', 'sum', 'mean', 'std'])
    df['size'] = df['size'].apply(float)
    return df

print(continent(col='Population'))