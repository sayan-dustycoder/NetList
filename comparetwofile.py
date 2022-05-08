import pandas as pd
df1 = pd.read_csv('processed_data/allegro_netlist-f.csv')
df1['column_one']=df1['column_one'].str.upper()
df1['column_two']=df1['column_two'].str.upper()
df2 = pd.read_csv('processed_data/Xpedition_Netlist_report-f.csv')
df2['column_three']=df2['column_three'].str.upper()
df2['column_four']=df2['column_four'].str.upper()
pd.set_option('display.max_rows', None)
result=df1[~df1.apply(tuple,1).isin(df2.apply(tuple,1))]
print("The components not matching: ")
print(result)
f = open('foo.txt', 'w') 
print(result,file=f) 
f.close() 
