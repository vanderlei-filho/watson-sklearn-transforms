from sklearn.base import BaseEstimator, TransformerMixin

#  RRR Definimos una función para no tener que usar valores texto
def valorIndx (valProfile):
    if   valProfile == "beginner_front_end":
        return 1
    elif valProfile == "advanced_front_end":
        return 2
    elif valProfile == "beginner_data_science":
        return 3
    elif valProfile == "advanced_data_science":
        return 4
    elif valProfile == "beginner_backend":    
        return 5
    elif valProfile == "advanced_backend":
        return 6
    else:  
        return 0

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # RRR la columna PROFILEnum substituira a la columna PROFILE
        data["PROFILEnum"] =  data["PROFILE"].apply (valorIndx)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
