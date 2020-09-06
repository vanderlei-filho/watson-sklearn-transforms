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
        # RR agregamos tres columnas que expresan la relacion entre columnas significativas segun mi criterio (revisar class MinimColumns más adelante )
        
        data["Rel_CXP_CXC"] =  data["CXC"] / data["CXP"]
        data["Rel_Bruta_U_P"] =  data["UTILIDAD_BRUTA"] / data["UTILIDAD_O_PERDIDA"]
        data["Rel_TV_U_P"] =  data["TOTAL_VENTAS"] / data["UTILIDAD_O_PERDIDA"]
        
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
    # RR  se requieren aplicar un criterio de minimo aceptable segun cada relación

"""
en mi excel, los vaores minimo son
CXP / CXC > 1.2
Utilidad_Bruta / Utilidad > 4 
Total Ventas / Utilidad > 35

"""

def minimo_CXP_CXC ( CXP_CXC):
        if   CXP_CXC > 1 :
            return 1000
        elif CXP_CXC == 0 :
            return 1000 / 3
        else:
            return 0
        

def minimo_Bruta_U_P ( Bruta_U_P):
        if   Bruta_U_P > 4 :
            return 1000
        elif Bruta_U_P == 0 :
            return 1000 / 3
        else:
            return 100
        

def minimo_TV_U_P ( TV_U_P):
        if   TV_U_P > 35 :
            return 1000
        elif TV_U_P == 0 :
            return 1000 / 3
        else:
            return 100
        


# All sklearn Transforms must have the `transform` and `fit` methods
class MinimColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # RR Agregamos las columnas indicadoras de que sí cumplen con los mínimos establecidos por mi excel
        
        data["minimo_CXP_CXC"] = data["Rel_CXP_CXC"].apply (minimo_CXP_CXC)
        # RR no aplicar data["minimo_Bruta_U_P"] = data["Rel_Bruta_U_P"].apply (minimo_Bruta_U_P) 
        # RR no aplicar data["minimo_TV_U_P"] = data["Rel_TV_U_P"].apply (minimo_TV_U_P) 
        
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')

    
    
# RR Desafio2    
class DropColumnsDesaf2(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
