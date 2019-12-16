Hard to Count Populations and the U.S. Census: Exploring Correlation Between Response Rate and Funding

This project uses publicly available Census Bureau data to explore the correlation between response rate and resource allocation as tied to the decennial U.S. Census and American Community Survey (ACS), with an eye specifically on different populations at the state and then national level.

Of course, the process of allocating funds is complex, with many factors. For manageability, this project plots 2010 mail-in rates (taken from the Census Bureau’s Planning Database) in relation to aggregate Community Development Block Fund Grants (CDBG) as representations of response rate and funding, respectively. (Based on my research, these were the most closely linked and indicative.) Tract markers are then color-coded according to percentage of the combined hard-to-count populations of Black and Hispanic.

Python was used to extract, transform and load, utilizing CSVs available online, and the Seaborn and Matplotlib libraries were used to generate the scatter plots.  However, while visualization is a large part of this project (and its exploration and refinement was time consuming), I came to see its role as exploratory, and not as a public-facing expression of census justice for a broad audience. The code is a kind of customizable tool, in which one could update just a couple of fields and generate comparisons, or confirm informed suppositions. For this reason, every effort was made to keep the project self-contained within Python, without the use of separate visualization software.

-----------------------------------------------

USING THE CODE AND FILES

As the project explored both each state individually and all states at once, there are two main folders
All_States_Code
Each_State_Code

Each then has subfolders for “_Initial_Visualization” and “_for_Updates”.

The “_Initial_Visualization” for each has two csv files, CDBG_Activity_by_Tract_112819.csv and PDB_2019trv3_us_112819.csv (which is zipped, due to size).

Running the python file in each of those folders on the two csvs will produce the new combined csvs, pngs and pdfs found in the “Resulting_Files” folder for each.*

The “_for_Updates” subfolder for each Code folder contains the csv files that resulted from the initial visualization. Therefore each ‘updates’ python file can be modified and run on its corresponding csvs. The intent of these files is for visualization refinement, as removing the csv generation from the process results in astronomical time savings. (Running the csv generation and visualization for each state takes approximately six hours; running just the visualization on pre-generated state csvs takes under five minutes.)

*Note: the “Each_State_for_Updates” folder doesn’t have a “Resulting_Files” folder, since all of its explorations have been folded into the initial visualization at this point.

