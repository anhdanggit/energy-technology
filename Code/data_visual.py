

def plot_explore(save):
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    Top15 = (pd.read_csv("../Data/cleaned_data.csv")
             .set_index('Country'))
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
    plt.show()

    if save == True:
        plt.savefig(os.path.abspath('../Results/data_visual.png'))


plot_explore(save=True)