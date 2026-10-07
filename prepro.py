import pandas as pd
df=pd.DataFrame({
    'Name':["arjun","melissa","sahasra","srihitha"],
    'age':[20,16,13,None]
})
d2 = pd.DataFrame({
    "grade": ["A", "B", "C", "C"],
    "age": [16, 20, 13, 16.33]
})
df['age']=df["age"].fillna(df['age'].mean())
df=df.drop_duplicates()

print(df)

data=pd.merge(df,d2,on="age")
print(data)
d2['age']=-(d2['age']-d2['age'].min())/(d2['age'].min()-d2['age'].max())
print(d2)