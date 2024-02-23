# coding:utf-8
# カテゴリカルデータのエンコード
# 順序特徴量のエンコード

import pandas as pd

# サンプルデータの生成
df = pd.DataFrame([
    ['green', 'M', 10.1, 'class2'],
    ['red', 'L', 13.5, 'class1'],
    ['blue', 'XL', 15.3, 'class2'],])

print(df)

print("------------------------------")

# 名列を設定
df.columns = ['color', 'size', 'price', 'classlabel']
print(df)

print("------------------------------")

# sizeは順序特徴量であるが、マシンは判別できないため、明示的に判別してあげる必要がある
size_mapping = {'XL': 3, 'L': 2, 'M': 1}
# サイズを整数に変換
df['size'] = df['size'].map(size_mapping)

print(df)
