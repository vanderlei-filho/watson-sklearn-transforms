# All sklearn Transforms must have the `transform` and `fit` methods
from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data = data.drop(labels=self.columns, axis='columns')
        data = data.dropna(axis=0, subset=["NOTA_GO"])
        df = data[['NOTA_DE' , 'NOTA_EM' , 'NOTA_MF' , 'NOTA_GO']]
        data['MEDIA'] = df.mean(axis=1)
        data['SOMA'] = df.sum(axis=1)
        df = data[['NOTA_DE' , 'NOTA_EM', 'NOTA_GO']]
        data['MEDIA_HUMANAS'] = df.mean(axis=1)
        return data

class Coding():
    def __init__(self, p):
        self.p = p

    def decode(self):
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

    def code(self):
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
