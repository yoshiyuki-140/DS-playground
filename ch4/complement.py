# coding:utf-8

from sklearn.impute import SimpleImputer
import numpy as np
import pickle


load_file_path = "sample_dataFrame.pkl"

with open(file=load_file_path, mode='rb') as f:
    df = pickle.load(f)

print(df.isnull().sum())
print(df.info())

# 欠損値補完のインスタンスを生成
imr = SimpleImputer(missing_values=np.nan, strategy='mean')

# データに適合させる
tmr = imr.fit(df.values)
