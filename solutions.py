import pandas as pd # type: ignore

df = pd.read_csv('./Application.csv')

print(df.to_string()) 