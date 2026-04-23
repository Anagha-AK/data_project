import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data.csv')
print("Full data:\n",data)
data['result']=data['marks']>40
print("\nTop student:\n",data.loc[data['marks'].idxmax()])
print("\nMarks >80:\n",data[data['marks']>80])
print("Highest marks:",data['marks'].max())
print("Lowest marks:",data['marks'].min())
print("Average marks:",data['marks'].mean())
data=data.sort_values('marks',ascending=False)
print("\nData sorted by marks:\n",data)

print(data.groupby('result')['marks'].mean())
print(data['result'].value_counts())
def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'Fail'

data['grade']=data['marks'].apply(grade)
print("\nStudents per grade:")
print(data['grade'].value_counts())
print(data.groupby('grade')['marks'].mean())
data['marks'].plot(kind='bar')
plt.show()

