
import pandas as pd

class DataLoader:
    """
        iterable yielding rows
        (("gender", 0), ("class", 2), ..., ("survived", 1))
    """

    def __init__(self, df:pd.DataFrame):
        self.df = df

    def __iter__(self):
        for row in self.df.iterrows():
            yield tuple(row[1].to_dict().items())


class DataLoaderDict(DataLoader):

    def __iter__(self):
        for row in self.df.iterrows():
            yield row[1].to_dict()