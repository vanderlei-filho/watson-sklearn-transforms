# All sklearn Transforms must have the `transform` and `fit` methods
# You can declare several custom transforms (as different classes) in
# this file


class DropColumns(object):
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X):
        # Criamos uma cópia do DataFrame e realizamos o drop das colunas desejadas
        return X.copy().drop(labels=self.columns, axis='columns')

    def fit(self, X, y=None):
        return self
