import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#define functions for percentage of population and per capita funding
def percentage(segment, total_pop):
    try:
        percent = (int(segment) / int(total_pop)) * 100
    except:
        percent = False
    return percent

def percapita(funding, total_pop):
    try:
        average = (float(funding) / int(total_pop))
    except:
        average = False
    return average


with open('AllStates_Tracts_BorH_121519.csv', 'w', newline='') as csvfile:
    fieldnames = ['State', 'County', 'Tract', 'Population', 'Black', 'Hispanic', 'Mail-In', 'CDBG Total', 'CDBG per person', 'Black or Hispanic (%)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
#first csv - Public Database
    with open("PDB_2019trv3_us_112819.csv", "r", encoding = 'cp1252') as file1:
        results = csv.reader(file1)
#skip headers
        next(results, None)
        for row in results:
#skipping rows that have glitch resulting in blank cell for Hispanic population
#printing the row allows me to track that 22 rows are skipped out of 74,000+
            if row[45] == '':
                print(row[0], 'Skipping track for empty row[45]')
                continue

#[45] is Hispanic population, [51] is Black population, [13] is total pop Census, all 2010
            percent_b_or_h = percentage(int(row[45]) + int(row[51]), row[13])
#282 is mail return rate
            if row[282] != "" and int(row[13]) > 500:
#no need to identify state; added the last qualifier to remove outliers (census tracts with less than 500 residents)
#now second csv - Community Development Block Grant activity
                with open("CDBG_Activity_by_Tract_112819.csv", "r", encoding = 'cp1252') as file2:
                    results2 = csv.reader(file2)
#skip headers
                    next(results2, None)
#matching tract IDs from csv 1 and csv 2
                    for line in results2:
                        if line[1] == row[0]:
                            block_funding = percapita(line[25],row[13])
                            writer.writerow({'State': row[2], 'County': row[4], 'Tract': row[0], 'Population': row[13], 'Black': row[51], 'Hispanic': row[45], 'Mail-In': row[282], 'CDBG Total': line[25], 'CDBG per person': round(block_funding, 1), 'Black or Hispanic (%)': round(percent_b_or_h, 1)})

#combined csv has been created; move on to creating scatter plot, using single file name
census_to_plot = pd.read_csv('AllStates_Tracts_BorH_121519.csv')
census_to_plot.head()
#some basic styling
sns.set(style="whitegrid")
sns.color_palette('copper_r')
fig, ax = plt.subplots(figsize=(16,16))
#establishing columns from combined csv to plot, along with soem styling, such as palette and transparency
sns.scatterplot(x='Mail-In', y='CDBG per person',
        hue='Black or Hispanic (%)',
        hue_order='Black or Hispanic (%)',
        hue_norm=(20,90),
        palette = 'copper_r',
        # edgecolor = 'none',
        alpha = .5,
        data = census_to_plot)
#creating legend, setting axis limits and adding labels and title
plt.legend(frameon=True, loc='upper left')
plt.ylim(0,500)
plt.xlim(0,100)
plt.xlabel('2010 Mail-In Response Rate', fontsize=25)
plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=25)
plt.title('All U.S. States (plus PR and DC): \nResponse Rate and Funding', weight='bold', fontsize=40, loc='left')
#saving the plots out as two file types for separate uses
plt.savefig('AllStates_Tracts_BorH_121519.pdf')
plt.savefig('AllStates_Tracts_BorH_121519.png')
#just because I like to print 'done' at the end
print("done")
#end of code
