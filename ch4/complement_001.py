# coding:utf-8
# データ補完のメソッドが書いてあるファイル

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

# 補完を実行
imputed_data = imr.transform(df.values)
print(imputed_data)
