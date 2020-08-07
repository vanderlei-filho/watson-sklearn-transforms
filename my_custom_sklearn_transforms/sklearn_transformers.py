from sklearn.base import BaseEstimator, TransformerMixin
# import numpy.lib.recfunctions as rf


# All sklearn Transforms must have the `transform` and `fit` methods
# You can declare several custom transforms (as different classes) in
# this file
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X):
        return X.copy().drop(labels=self.columns, axis='columns')
        # data = X.copy()
        # return rf.drop_fields(data, self.columns)

    def fit(self, X, y=None):
        return self
