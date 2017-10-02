
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

def corr_cit_sup():

    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['Population']
    answer = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return answer

print(corr_cit_sup())

# plot

# optional style
matplotlib.style.use('ggplot')


def plot_cit_sup(save):

    Top15 = pd.read_csv("../Data/cleaned_data.csv")
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    plt.show()
    if save == 'True':
        plt.savefig(os.path.abspath('../Results/corr_cit_sup.png'))

plot_cit_sup(save='False')
