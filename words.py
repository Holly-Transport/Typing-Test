import pandas

class WordBank:

    def __init__(self):
        self.data = pandas.read_csv("WordBank.csv")

    def WordList (self):
        self.words = self.data.sample(75)
        return self.words.values.tolist()


