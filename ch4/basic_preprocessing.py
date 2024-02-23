# coding:utf-8
# 主な前処理が書いてあるファイル

import pandas as pd
from io import StringIO
import pickle

csv_data = '''A,B,C,D
1.0,2.0,3.0,4.0
5,6,7,8
10,11,12'''

df = pd.read_csv(StringIO(csv_data))
save_file_path = "sample_dataFrame.pkl"
with open(file=save_file_path, mode='wb') as f:
    pickle.dump(df, f)

if __name__ == "__main__":
    print(df)

    print("-------------------")

    # 各特徴量の欠損値をカウント
    print(df.isnull().sum())

    print("-------------------")

    # 欠損値をを含んでいる行を削除
    print(df.dropna(axis=1))

    print("-------------------")

    # 欠損値を含んでいる列(カラム)を削除
    print(df.dropna(axis=1))

    print("-------------------")

    # 全ての列がNaNである行だけを削除
    print(df.dropna(how='all'))

    print("-------------------")

    # 非NaN値が4つ未満の行を削除
    print(df.dropna(thresh=4))

    print("-------------------")

    # 特定の列（この場合は'C'）にNaNが含まれている行だけを削除
    print(df.dropna(subset=['C']))
