import pandas as pd


#Creating a pivot table
df = pd.read_excel('supermarket_sales.xlsx')  #create dataframe from excel file
# print(df)

df = df[['Gender', 'Product line', 'Total']]  #only 3 col selected

pivotTable = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum') # goal is to see how much each gender spends in each product line

pivotTable.to_excel('pivot_table.xlsx', 'Report', startrow=4)