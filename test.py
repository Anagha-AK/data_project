import pandas as pd

data=pd.read_csv('data.csv')
print("Full data:\n",data)
print("\nAverage marks:",data['marks'].mean())
print("\nTop student:\n",data.loc[data['marks'].idxmax()])
print("\nMarks >80:\n",data[data['marks']>80])
data=data.sort_values('marks',ascending=False)
print("\nData sorted by marks:\n",data)
print("Highest marks:",data['marks'].max())
print("Lowest marks:",data['marks'].min())
print("Average marks:",data['marks'].mean())
print(data.groupby('name')['marks'].mean())