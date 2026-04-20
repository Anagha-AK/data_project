import pandas as pd
data=pd.read_csv('sales.csv')
print("Full data:\n",data)

data['total']=data['price']*data['quantity']
print("\nData with total:\n",data)
print("Total revenue:",data['total'].sum())
print("Highest selling product:\n",data.loc[data['total'].idxmax()])
data=data.sort_values('total',ascending=False)
print("\nData sorted by total:\n",data)