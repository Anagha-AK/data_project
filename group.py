import pandas as pd
data=pd.read_csv('group.csv')
print("Full data:\n",data)
grouped=data.groupby('category')['amount'].sum()
print("\nGrouped data:\n",grouped)
