# coding:utf-8

from sklearn.impute import SimpleImputer
import numpy as np
from basic_preprocessing import df

# 欠損値補完のインスタンスを生成
imr = SimpleImputer(missing_values=np.nan, strategy='mean')

# データに適合させる
tmr = imr.fit(df.values)
