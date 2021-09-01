#import csv
import pandas as pd
df = pd.read_csv("GLOBAL_PRODUCTION_QUANTITY_OCEANIA.csv")
cc = pd.read_csv("CL_FL_COUNTRYGROUPS_OCEANIA.csv")
df['COUNTRY'] = cc['Official_Name_En']
df.to_csv("newTest.csv")



# def read_csv(filename):
#     results = []
#     with open('GLOBAL_PRODUCTION_QUANTITY_OCEANIA.csv', 'r') as f:
#         myreader = csv.reader(f)
#         writer = csv.writer(f)
#         for row in myreader:
#             'COUNTRY.UN_CODE', 'SPECIES.ALPHA_3_CODE', 'PERIOD', 'VALUE', 'STATUS'
#             results.append(row)
#             writer.writerow(row)
#     return results 



# def clean_data(filename):
#     # Process csv into python readable format
#     data = read_csv(filename)

#     # Check that none of the column is empty
#     data = list(filter(lambda x: x[0] != "" and x[1] != "" and x[2]
#                 "" and x[3] != "" and x[4] != "" and x[5] != "", data))
#     # another way using a second filter
#     # data = list(filter(lambda x: len(list(filter(lambda y:y!="",x)))==6,data))

#     # Check that movie is within timespan
#     data = list(filter(lambda x: 1990 <= int(x[5]) <= 2019, data))

#     # Check that movie rating is within range
#     data = list(filter(lambda x: 0 <= float(x[4]) <= 10, data))

#     # Check that movie rating is higher than 9
#     data = list(filter(lambda x: float(x[4]) >= 9, data))

#     # Returns only a list of movie names
#     return list(map(lambda x: x[3], data))
