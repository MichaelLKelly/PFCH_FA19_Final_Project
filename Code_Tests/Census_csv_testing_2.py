import csv



def percentage(total_pop, segment):
    try:
        percent = (int(total_pop) / int(segment)) * 100
    except:
        percent = False
    return percent



#open public database?
# with open("pdb2019trv3_us.csv", "r", encoding = 'cp1252') as file1:
#     results = csv.reader(file1)
#skip headers
    # next(results, None)


with open('census_combine_test.csv', 'w', newline='') as csvfile:
    fieldnames = ['State', 'County', 'Tract', 'Mail-In', 'Low', 'Ten', 'Males (%)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    with open("pdb2019trv3_us.csv", "r", encoding = 'cp1252') as file1:
        results = csv.reader(file1)
    #skip headers
        next(results, None)
        for row in results:
            percent_male = percentage(row[16], row[13])

            if row[2] == 'New York' and row[4] == "Kings County" and row[282] != "" and float(row[282]) < 60 or row[2] == 'Oklahoma' and row[4] == "Tulsa County" and row[282] != "" and float(row[282]) < 60:

#could someone input the values above???

            # print(row[2],row[4],row[0],row[282],row[283])
                with open("Community_Development_Block_Grant_Activity_by_Tract.csv", "r", encoding = 'cp1252') as file2:
                    results2 = csv.reader(file2)



                    next(results2, None)
                    for line in results2:
                        if line[1] == row[0]:
                        # print(row[2],row[4],row[0],row[282],row[283],line[10])

                            writer.writerow({'State': row[2], 'County': row[4], 'Tract': row[0], 'Mail-In': row[282], 'Low': row[283], 'Ten': line[10], 'Males (%)': round(percent_male, 1)})



with open('census_combine_test.csv', 'r') as newdict:
    new_results = csv.reader(newdict)

    for item in new_results:
        print(item[0])


    # for row in results:
    #     if row[2] == 'New York' and row[4] == "Kings County" and row[282] != "" and float(row[282]) < 70:
    #         # print(row[2],row[4],row[0],row[282],row[283])
    #         with open("Community_Development_Block_Grant_Activity_by_Tract.csv", "r", encoding = 'cp1252') as file2:
    #             results2 = csv.reader(file2)
    #
    #             next(results2, None)
    #             for line in results2:
    #                 if line[1] == row[0]:
    #                     # print(row[2],row[4],row[0],row[282],row[283],line[10])
    #                     with open('census_combine_test.csv', 'w', newline='') as csvfile:
    #                         fieldnames = ['State', 'County', 'Tract', 'Mail-In', 'Low', 'Ten']
    #                         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #                         writer.writeheader()
    #                         writer.writerow({'State': row[2], 'County': row[4], 'Tract': row[0], 'Mail-In': row[282], 'Low': row[283], 'Ten': line[10]})



print("done")
