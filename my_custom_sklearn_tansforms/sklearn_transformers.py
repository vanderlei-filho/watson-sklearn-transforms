# All sklearn Transforms must have the `transform` and `fit` methods
# You can declare several custom transforms (as different classes) in
# this file


class DropColumns(object):
    def __init__(self, columns):
        self.columns = columns

    def transform(self, x):
        return x.copy().drop(labels=self.columns, axis='columns')

    def fit(self, df, y=None):
        return self
