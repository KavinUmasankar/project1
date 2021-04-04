import numpy as np
import pandas as pd
df = pd.read_csv("C:/Kavin/Python/Projects/project1/data/data.csv")
for column in df.columns:
    df[column] = df[column].replace(np.nan, 0)
print(df)