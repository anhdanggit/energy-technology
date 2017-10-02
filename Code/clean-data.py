import pandas as pd
import numpy as np
import os, re

"""Energy Indicators Data"""

# reading data
energy = (pd.read_excel("../Data/Energy Indicators.xls", header=17, skip_footer=38, parse_cols="C:G")
          .reset_index()
          .replace('...', np.nan))  # replace '...'


energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'] # change col labels
energy['Country'] = energy['Country'].str.replace('\d+','')  # replace digits in 'Country' col
energy['Energy Supply'] = energy['Energy Supply'] * 1000000  # convert Energy Supply

di = {"Republic of Korea": "South Korea",
      "United States of America": "United States",
      "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
      "China, Hong Kong Special Administrative Region": "Hong Kong"}

energy = energy.replace({'Country': di})  # TRICK: Use the dict. to change values

# remove characters inside the parenthesis
energy['Country'] = energy.apply(lambda x: re.sub(r' \([^()]*\)', '', x['Country']), axis=1)
energy = energy.set_index('Country')


"""GDP Data"""
di = {"Korea, Rep.": "South Korea",
         "Iran, Islamic Rep.": "Iran",
         "Hong Kong SAR, China": "Hong Kong"}

GDP = (pd.read_csv("../Data/world_bank.csv", header=2)
      .rename(columns={'Country Name': 'Country'})
      .replace({'Country': di})
      .set_index('Country')
      .loc[:, '2006':'2015'])


"""ScimEn Data"""
ScimEn = pd.read_excel('../Data/scimagojr.xlsx', index_col='Country')
ScimEn = ScimEn[ScimEn['Rank'] < 16]  # take Top 15

"""Merge ScimEn, energy, and GDP"""

df_temp = pd.merge(ScimEn, energy, how='inner', left_index=True, right_index=True)
df = pd.merge(df_temp, GDP, how='inner', left_index=True, right_index=True)

"""Save the cleaned data as csv file"""

df.to_csv('../Data/cleaned_data.csv')
