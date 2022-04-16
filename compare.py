import pandas as pd

# read csv files
df1 = pd.read_csv('processed_data/processed_data.csv')
df2 = pd.read_csv('processed_data/processed_data1.csv')

match = True        # to check matches of two files
unmatch = []        # to add components which show anomaly

for index in df1.index:     # traverse through df1
    name1 = ""
    name2 = ""
    component_name = df1['column_two'][index]       # to get component name to check
    index1 = df1[df1['column_two'] == component_name].index.values      # to get index of component in df1
    for ind in index1:
        name1 = df1['column_one'][ind]
    index2 = df2[df2['column_two'] == component_name].index.values      # to get index of component in df2
    for ind in index2:
        name2 = df2['column_one'][ind]
    if name2 != name1:
        match = False
        unmatch.append(component_name)

if match:
    print("NetList Match Successful!")
else:
    print("NetList Match Unsuccessful")
    print("The components not matching: ")
    for component in unmatch:
        print(component)

# component_name = df1['column_two'][1]
# index1 = df1[df1['column_two'] == component_name].index.values
# print(component_name)
# for index in index1:
#     print(df1['column_one'][index])
# print()
# index2 = df2[df2['column_two'] == component_name].index.values
# print(df2['column_two'][index2])
# name = df2['column_one'][index2]
# # print(name)
# for index in index2:
#     print(df2['column_one'][index])
