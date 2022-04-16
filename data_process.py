#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv


# In[2]:


def find_first_occurence_of_add_ter(original_data):
    add_ter_index = -1
    for i in range(0, len(original_data)):
        if ".ADD_TER" in original_data[i]:
            add_ter_index = i
            break
    
    return add_ter_index


# In[3]:


def get_mappings(focused_data):
    final_data = list()
    
    column_one = ""
    column_two = ""
    for i in focused_data:
        # Updating column one if the row is .ADD_TER
        if ".ADD_TER" in i:
            column_one = i[3]
            
        # Updating the column two details
        if ".ADD_TER" in i or ".TER" in i:
            column_two = i[1] + i[2]
        else:
            column_two = i[0] + i[1]
        
        temp_dict = {
            "column_one": column_one,
            "column_two": column_two
        }
        final_data.append(temp_dict)
    
    return final_data
        


# In[4]:


def dump_final_data_to_file(final_data, filename):
    final_filename = "processed_data/" + filename
    
    with open(final_filename, mode='a+') as csv_file:
        fieldnames = ['column_one', 'column_two']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(final_data)
    
    print("final_data written to ", final_filename)
    

# In[5]:


def process_data(filename, output_csv_filename):
    # Load the file to process
    original_data = list()
    delim = "  "
    with open(filename) as file:     
        for line in file.readlines():
            temp_list = line.split()
            if temp_list != []:
                original_data.append(line.split())
              
    # Process the file and get the mappings
    first_occurence_of_add_ter = find_first_occurence_of_add_ter(original_data)
    if first_occurence_of_add_ter != -1:
        focused_data = original_data[first_occurence_of_add_ter:-1]
        final_data = get_mappings(focused_data)
        dump_final_data_to_file(final_data, output_csv_filename)

    else:
        print("Cannot find .ADD_TER in the data file, exiting...")


def remove_quotations(processed_data):
    df1=pd.read_csv(processed_data)
    df1=df1.applymap(lambda x: x.replace('"', ''))
    return df1


# In[6]:
while True:
    option = int(input("Enter 1 to convert a NetList or 0 to quit"))
    
    if option == 0:
        break

    fileName1 = input("Enter the name of the first NetList file to check")
    fileName2 = input("Enter the name of the second NetList file to check")
    destinationFile1 = input("Enter the name of the csv file to store the converted data into")
    destinationFile2 = input("Enter the name of the csv file to store the converted data into")
    filename_list = [fileName1, fileName2]
    for index, fileName in enumerate(filename_list):
        file_name = "destinationFile"+str(index+1)
        position = fileName.find('.')
        netlist_format = fileName[position+1:]

        if netlist_format == 'txt':
            process_data(fileName, file_name)
            df = pd.read_csv(file_name)
            if '"' in df.column_two[0]: 
                df = remove_quotations(file_name)
                df.to_csv(file_name)

# In[7]:


# test one file

# process_data("data.txt","processed_data.csv" )

# import csv
# file = open("processed_data.csv")
# csvreader = csv.reader(file)
# header = next(csvreader)
# print(header)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
# file.close()


# # In[8]:


# import pandas as pd
# df1=pd.read_csv("processed_data.csv")


# # In[9]:


# df1
