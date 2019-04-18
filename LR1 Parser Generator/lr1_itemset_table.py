from first_follow_generator import FirstFollowGenerator

class Item:
    def __init__(self, rules, id, next):
        self.rules = []
        self.id = None
        self.haveNext = False

    def get(self):
        print("i", id, end = "")
        print("Final? ", self.haveNext, end = "")
        print("Rules: ", self.rules)

class Itemset_LR1:
    def __init__(self, rules):
        self.items = []

def generateParsingTable(non_terminal, terminal, rules):
    ffg = FirstFollowGenerator(non_terminal, terminal, rules)


non_terminal = ['S*', 'S', 'C']
terminal = ['c', 'd']
rules = [['S*', 'S'], ['S', 'C', 'C'], ['C', 'c', 'C'], ['C', 'd']]
generateParsingTable(non_terminal,terminal,rules)