
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

census_to_plot = pd.read_csv('AllStates_Tracts_BorH_121519.csv')
census_to_plot.head()

sns.set(style="whitegrid")
sns.color_palette('copper_r')
fig, ax = plt.subplots(figsize=(16,16))

sns.scatterplot(x='Mail-In', y='CDBG per person',
        hue='Black or Hispanic (%)',
        hue_order='Black or Hispanic (%)',
        hue_norm=(20,90),
        palette = 'copper_r',
        # edgecolor = 'none',
        alpha = .5,
        data = census_to_plot)

plt.legend(frameon=True, loc='upper left')
plt.ylim(0,500)
plt.xlim(0,100)
plt.xlabel('2010 Mail-In Response Rate', fontsize=25)
plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=25)
plt.title('All U.S. States (plus PR and DC): \nResponse Rate and Funding', weight='bold', fontsize=40, loc='left')

plt.savefig('AllStates_Tracts_BorH_121519_16x16.pdf')
plt.savefig('AllStates_Tracts_BorH_121519_16x16.png')

print("16x16 done")

#new test update ---------------

census_to_plot = pd.read_csv('AllStates_Tracts_BorH_121519.csv')
census_to_plot.head()

sns.set(style="whitegrid")
sns.color_palette('copper_r')
fig, ax = plt.subplots(figsize=(8,8))

sns.scatterplot(x='Mail-In', y='CDBG per person',
        hue='Black or Hispanic (%)',
        hue_order='Black or Hispanic (%)',
        hue_norm=(20,90),
        palette = 'copper_r',
        # edgecolor = 'none',
        alpha = .5,
        data = census_to_plot)

plt.legend(frameon=True, loc='upper left')
plt.ylim(0,500)
plt.xlim(0,100)
plt.xlabel('2010 Mail-In Response Rate', fontsize=15)
plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=15)
plt.title('All U.S. States (plus PR and DC): \nResponse Rate and Funding', weight='bold', fontsize=20, loc='left')

plt.savefig('AllStates_Tracts_BorH_121519_8x8.pdf')
plt.savefig('AllStates_Tracts_BorH_121519_8x8.png')

print("8x8 done")

#new test update ---------------

census_to_plot = pd.read_csv('AllStates_Tracts_BorH_121519.csv')
census_to_plot.head()

sns.set(style="whitegrid")
sns.color_palette('copper_r')
fig, ax = plt.subplots(figsize=(24,24))

sns.scatterplot(x='Mail-In', y='CDBG per person',
        hue='Black or Hispanic (%)',
        hue_order='Black or Hispanic (%)',
        hue_norm=(20,90),
        palette = 'copper_r',
        # edgecolor = 'none',
        alpha = .5,
        data = census_to_plot)

plt.legend(frameon=True, loc='upper left')
plt.ylim(0,500)
plt.xlim(0,100)
plt.xlabel('2010 Mail-In Response Rate', fontsize=35)
plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=35)
plt.title('All U.S. States (plus PR and DC): \nResponse Rate and Funding', weight='bold', fontsize=60, loc='left')

plt.savefig('AllStates_Tracts_BorH_121519_24x24.pdf')
plt.savefig('AllStates_Tracts_BorH_121519_24x24.png')

print("24x24 done")
