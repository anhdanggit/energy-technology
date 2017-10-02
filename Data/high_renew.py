
def high_renew():
    import pandas as pd
    import numpy as np
    Top15 = (pd.read_csv("../Data/cleaned_data.csv")
             .set_index('Country')
             .sort_values('Rank', ascending=True)) # sorting by rank
    median = np.median(Top15['% Renewable'])

    def highrenew(df):
        if df['% Renewable'] < median:
            df['HighRenew'] = 0
        else:
            df['HighRenew'] = 1
        return df

    Top15 = Top15.apply(highrenew, axis=1)
    return Top15['HighRenew']

print(high_renew())
