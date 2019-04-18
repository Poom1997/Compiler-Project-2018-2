
class FirstFollowGenerator:
    def __init__(self, non_terminal, terminal, rules):
        self.non_terminal = non_terminal
        self.terminal = terminal
        self.rules = rules
        self.first = []
        self.follow = []
        self.generate_first()
        self.generate_follow()

    def generate_first(self):
        for each_item in self.non_terminal:
            temp = []
            temp.append(each_item)
            explore = each_item
            for rule in rules:
                if(explore == rule[0]):
                    if(rule[1] in self.terminal):
                        temp.append(rule[1])
                    else:
                        explore = rule[1]
            self.first.append(temp)

    def generate_follow(self):
        temp = [self.non_terminal[0], '$']
        self.follow.append(temp)
        for each_item in self.non_terminal[1:]:
            temp = [each_item]
            for rule in rules:
                for i in range(1, len(rule)):
                    if (each_item == rule[i]):
                        if (i < len(rule) - 1):
                            if (rule[i + 1] in terminal):
                                temp.append(rule[i + 1])
                            else:
                                self_first = self.get_first_of(rule[i + 1])
                                temp = temp + self_first
                        else:
                            if (rule[0] != rule[i]):
                                self_follow = self.get_follow_of(rule[0])
                                temp = temp + self_follow
                            else:
                                continue
            # Remove duplicates
            temp = list(dict.fromkeys(temp))
            self.follow.append(temp)

    def get_first_of(self, symbol):
        for each_element in self.first:
            if (each_element[0] == symbol):
                return each_element[1:]
        return []

    def get_follow_of(self, symbol):
        for each_element in self.follow:
            if (each_element[0] == symbol):
                return each_element[1:]
        return []

    def get_first(self):
        return self.first

    def get_follow(self):
        return self.follow

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