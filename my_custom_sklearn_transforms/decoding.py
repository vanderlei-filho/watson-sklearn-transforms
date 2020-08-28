import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class Decoding(BaseEstimator, TransformerMixin):
    def __init__(self, p):
        self.p = p

    def fit(self):
        return self.p
    
    def transform(self):
        self.p1 = np.array([])
        for i in range(0,len(self.p)):
            if self.p[i] <= 1.0:
                self.p1 = np.append(self.p1, "EXCELENTE")
            if self.p[i] == 2.0:
                self.p1 = np.append(self.p1, "MUITO_BOM")
            if self.p[i] == 3.0:
                self.p1 = np.append(self.p1, "HUMANAS")
            if self.p[i] == 4.0:
                self.p1 = np.append(self.p1, "EXATAS")
            if self.p[i] >= 5.0:
                self.p1 = np.append(self.p1, "DIFICULDADE")
        return self.p1
