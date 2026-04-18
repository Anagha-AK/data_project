import pandas as pd

data=pd.read_csv('data.csv')
print("Full data:\n",data)
print("\nAverage marks:",data['marks'].mean())
print("\nTop student:\n",data.loc[data['marks'].idxmax()])
print("\nMarks >80:\n",data[data['marks']>80])