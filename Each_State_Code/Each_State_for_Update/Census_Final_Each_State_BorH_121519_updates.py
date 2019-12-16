import csv
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


list_of_states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico Commonwealth','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

loop_counter = 0

while loop_counter < 52:

    census_to_plot = pd.read_csv((list_of_states[loop_counter]) + '_Tracts_BorH_121519.csv')
    census_to_plot.head()

    sns.set(style="whitegrid")
    sns.color_palette('copper_r')
    fig, ax = plt.subplots(figsize=(8,8))

    sns.scatterplot(x='Mail-In', y='CDBG per person',
            hue='Black or Hispanic (%)',
            hue_order='Black or Hispanic (%)',
            hue_norm=(20,90),
            palette = ('copper_r'),
            # edgecolor = 'none',
            alpha = .6,
            data = census_to_plot)

    plt.legend(frameon=True, loc='upper left')
    plt.ylim(0,500)
    plt.xlim(0,100)
    plt.xlabel('2010 Mail-In Response Rate', fontsize=15)
    plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=15)
    plt.title((list_of_states[loop_counter]) + ' Census Tracts: \nResponse Rate and Funding', weight='bold', fontsize=20, loc='left')

    plt.savefig((list_of_states[loop_counter]) + '_Tracts_BorH_121519.pdf')
    plt.savefig((list_of_states[loop_counter]) + '_Tracts_BorH_121519.png')

    print((list_of_states[loop_counter]) + " done")

    loop_counter = loop_counter + 1

#end of code
