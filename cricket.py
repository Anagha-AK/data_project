import pandas as pd
data=pd.read_csv('cricket.csv')
print("Full data:\n",data)

data['average']=data['runs'] / data['matches']
print("\nData with average:\n",data)
print("Best Average:",data['average'].max())
data=data.sort_values('average',ascending=False)
print("Player with runs>9500:\n",data[data['runs']>9500])