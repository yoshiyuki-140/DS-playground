# coding:utf-8
# カテゴリカルデータのエンコード
# 名義特徴量のエンコード

import numpy as np

# クラスラベルと整数を対応させる辞書を生成
class_mapping = {lable: idx for idx, labl in enumerate(np.unique(df['']))}
