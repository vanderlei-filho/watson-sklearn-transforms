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
        return data.drop(labels=self.columns, axis='columns')

class Hours_Avg_Columns(BaseEstimator, TransformerMixin):
    def __init__(self):
        print ("Ya fue creado")

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        self.avg1  = data['AVG_SCORE_DATASCIENCE'].mean() * 2
        data['HOURS_AVG_DATASCIENCE'] = data['HOURS_DATASCIENCE'] / self.avg1
        
        self.avg2  = data['AVG_SCORE_BACKEND'].mean() * 2
        data['HOURS_AVG_BACKEND'] = data['HOURS_BACKEND'] / self.avg2
        
        self.avg3  = data['AVG_SCORE_FRONTEND'].mean() * 2
        data['HOURS_AVG_FRONTEND'] = data['HOURS_FRONTEND'] / self.avg3
        
        # Normalizamos las columnasde Horas, como el minimo en todos los casos es cero, es muy fácil
        self.Max1  = data['HOURS_DATASCIENCE'].max()
        data['HOURS_DATASCIENCE_norm'] = data['HOURS_DATASCIENCE'] / self.Max1
        data['AVG_SCORE_DATASCIENCE_norm'] =  data['AVG_SCORE_DATASCIENCE'] / 100
        
        self.Max2  = data['HOURS_BACKEND'].max()
        data['HOURS_BACKEND_norm'] = data['HOURS_BACKEND'] / self.Max2
        data['AVG_SCORE_BACKEND_norm'] =  data['AVG_SCORE_BACKEND'] / 100
        
        self.Max2  = data['HOURS_FRONTEND'].max()
        data['HOURS_FRONTEND_norm'] = data['HOURS_FRONTEND'] / self.Max2
        data['AVG_SCORE_FRONTEND_norm'] = data['AVG_SCORE_FRONTEND'] / 100
        
        return data


