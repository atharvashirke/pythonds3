class Card:

    def __init__(self, label):
        self.label = label

    def get_label(self):
        return self.label

class NormalCards(Card):

    def __init__(self, label):
        Card.__init__(self, label)
        self.suite = None

    def set_suite(self, suite):
        self.suite = suite

    def get_suite(self):
        return self.suite
