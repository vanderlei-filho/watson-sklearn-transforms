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
        df = df_data_1[['NOTA_DE' , 'NOTA_EM' , 'NOTA_MF' , 'NOTA_GO']]
        data['MEDIA'] = df.mean(axis=1)
        data['SOMA'] = df.sum(axis=1)
        df = df_data_1[['NOTA_DE' , 'NOTA_EM', 'NOTA_GO']]
        data['MEDIA_HUMANAS'] = df.mean(axis=1)
        return data
