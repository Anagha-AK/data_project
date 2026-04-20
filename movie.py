import pandas as pd
data=pd.read_csv('movie.csv')
print("Full data:\n",data)

print("\nHighest rated movie:",data.loc[data['rating'].idxmax()])
print("\nAverage rating:",data['rating'].mean())
print("\nMovies after 2023:\n",data[data['year']>2023])
print("\nAction movies:\n",data[data['genre']=='Action'])
data=data.sort_values('rating',ascending=False)