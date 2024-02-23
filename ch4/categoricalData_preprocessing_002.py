# coding:utf-8
# カテゴリカルデータのエンコード
# 名義特徴量のエンコード

import numpy as np
import pickle

# サンプルデータのロード
load_file_path = './sample_dataFrame_002.pkl'
with open(load_file_path, mode='rb') as f:
    df = pickle.load(f)

# クラスラベルと整数を対応させる辞書を生成
# class_mapping = {lable: idx for idx, labl in enumerate(np.unique(df['size']))}
