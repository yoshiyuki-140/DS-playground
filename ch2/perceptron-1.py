# coding:utf-8
# パーセプロトンの実装

import numpy as np


class Perceptoron:
    """パーセプトロン分類器
    パラメータ:
    ------------
    eta : float
        学習率(0.0より大きく1.0以下の値)
    n_iter : int
        トレーニングデータのトレーニング回数

    random_state : int
        重みを初期化するための乱数シード

    属性
    ------------
    w_ : 1次元配列
        適合後の重み
    b_ : スカラー
        適合後のバイアスユニット
    errors_ : リスト
        各エポックでの誤分類(更新)の数
    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """訓練データに適合させる

        Args:
            X (_type_): 訓練ベクトル:n_examplesは訓練データの個数,n_featureは特徴量の個数
            y (_type_): 目的変数

        戻り値:
            self : object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.float_(0.0)
        self.errors_ = []

        for _ in range(self.n_iter):  # 訓練データを繰り返し処理
            erros = 0
            for xi, target in zip(X, y):  # 重みとバイアスユニットを更新
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)  # 誤差を追加
            self.errors_.append(errors)
        return self

        pass
