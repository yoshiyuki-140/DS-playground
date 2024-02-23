# coding:utf-8
# カテゴリカルデータのエンコード
# 名義特徴量のエンコード

import numpy as np
import pickle

# サンプルデータのロード
load_file_path = './sample_dataFrame_002.pkl'
with open(load_file_path, mode='rb') as f:
    df = pickle.load(f)

print(df)

# クラスラベルと整数を対応させる辞書を生成
class_mapping = {label: idx for idx,
                 label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)

# 作成したマッピング用の辞書を使用し、クラスラベルを整数に変換する
df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)
