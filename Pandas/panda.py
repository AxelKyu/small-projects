import pandas as pd 

df = pd.read_csv('pokemon_data.csv')

print (df.iloc[2, 0])