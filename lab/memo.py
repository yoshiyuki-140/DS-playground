# coding:utf-8
import pandas as pd
from io import StringIO

csv_data = """
A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,,8.0
10.0,11.0,12.0,"""

df = pd.read_csv(StringIO(csv_data))
print(df)
print(df.dropna(axis=1).dropna(axis=0))
