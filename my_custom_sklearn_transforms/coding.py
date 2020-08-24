import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class Coding(BaseEstimator, TransformerMixin):
    def __init__(self, p):
        self.p = p

    def fit(self):
        return self.p
    
    def transform(self):
        self.p1 = np.array([])
        for i in range(0,len(self.p)):
            if self.p[i] == "EXCELENTE":
                self.p1 = np.append(self.p1, 1)
            if self.p[i] == "MUITO_BOM":
                self.p1 = np.append(self.p1, 2)
            if self.p[i] == "HUMANAS":
                self.p1 = np.append(self.p1, 3)
            if self.p[i] == "EXATAS":
                self.p1 = np.append(self.p1, 4)
            if self.p[i] == "DIFICULDADE":
                self.p1 = np.append(self.p1, 5)
        return self.p1
