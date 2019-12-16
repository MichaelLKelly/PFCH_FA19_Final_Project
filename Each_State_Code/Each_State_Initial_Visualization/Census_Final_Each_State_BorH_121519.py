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

#create list of states (plus PR and D of C) for looping through
list_of_states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico Commonwealth','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

#set loop counter for states (plus PR and D of C)
loop_counter = 0

while loop_counter < 52:
#use loop counter of state names to define file names and titles moving forward
    with open((list_of_states[loop_counter]) + '_Tracts_BorH_121519.csv', 'w', newline='') as csvfile:
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
                if row[2] == (list_of_states[loop_counter]) and row[282] != "" and int(row[13]) > 500:
#identifying if it's the state we want for this loop; added the last qualifier to remove outliers (census tracts with less than 500 residents)
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

#combined csv has been created; loop moves on to creating scatter plot, using file named with the loop counter name established earlier
    census_to_plot = pd.read_csv((list_of_states[loop_counter]) + '_Tracts_BorH_121519.csv')
    census_to_plot.head()
#some basic styling
    sns.set(style="whitegrid")
    sns.color_palette('copper_r')
    fig, ax = plt.subplots(figsize=(8,8))
#establishing columns from combined csv to plot, along with soem styling, such as palette and transparency
    sns.scatterplot(x='Mail-In', y='CDBG per person',
            hue='Black or Hispanic (%)',
            hue_order='Black or Hispanic (%)',
            hue_norm=(20,90),
            palette = ('copper_r'),
            # edgecolor = 'none',
            alpha = .6,
            data = census_to_plot)
#creating legend, setting axis limits and adding labels and title (using loop counter again)
    plt.legend(frameon=True, loc='upper left')
    plt.ylim(0,500)
    plt.xlim(0,100)
    plt.xlabel('2010 Mail-In Response Rate', fontsize=15)
    plt.ylabel('Aggregate Community Development Block Grants ($ per resident)', fontsize=15)
    plt.title((list_of_states[loop_counter]) + ' Census Tracts: \nResponse Rate and Funding', weight='bold', fontsize=20, loc='left')
#saving the plots out as two file types for separate uses
    plt.savefig((list_of_states[loop_counter]) + '_Tracts_BorH_121519.pdf')
    plt.savefig((list_of_states[loop_counter]) + '_Tracts_BorH_121519.png')
#printing a 'done' line for each state in terminal so progress can be tracked
    print((list_of_states[loop_counter]) + " done")
#preparing to move on to the next loop
    loop_counter = loop_counter + 1

#end of code
