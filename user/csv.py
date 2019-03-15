import pandas as pd
import numpy as np
df = pd.read_csv("/static/1.csv")
row=df.values.tolist()
print(row)