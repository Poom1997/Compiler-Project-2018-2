from first_follow_generator import FirstFollowGenerator

class Item:
    def __init__(self, rules, id, next):
        self.rules = rules
        self.id = id
        self.end = next

    def have_next(self):
        return self.end

    def getID(self):
        return self.id

    def getRules(self):
        return self.rules

    def getAll(self):
        print("S", self.id, end = " : ")
        print("Have_Next =", self.have_next(), end = " : ")
        print("Rules =", self.rules)

class Itemset_LR1:
    def __init__(self, non_terminal, terminal, rules):
        self.non_terminal = non_terminal
        self.terminal = terminal
        self.rules = rules
        self.items = []
        self.remaining = []
        self.transition = []
        self.currentNode = []
        self.id = 0
        self.init_states()
        self.expand_All_Items()


    def createItem(self, rule, next):
        item = Item(rule, self.id, next)
        self.remaining.append(item)
        self.id = self.id + 1

    def init_states(self):
        temp = [self.rules[0]]
        temp[0].insert(1, '.')
        start = temp[0]
        for i in range(0,len(start)):
            if(start[i] == '.'):
                if(start[i+1] in non_terminal):
                    expand = start[i+1]
                    for rule in self.rules:
                        temp_expand = []
                        if (expand == rule[0]):
                            for j in range(len(rule)):
                                if (j == 1):
                                    temp_expand.append('.')
                                    if (rule[j] in self.non_terminal):
                                        expand = rule[j]
                                temp_expand.append(rule[j])
                            temp.append(temp_expand)

        self.createItem(temp, False)

    def expand_All_Items(self):
        print(len(self.remaining))
        while(len(self.remaining) != 0):
            currentNode = self.remaining.pop(0)
            currentNodeX = Item(currentNode.getRules(), currentNode.getID(), currentNode.have_next())
            self.currentNode = Item(currentNode.getRules(), currentNode.getID(), currentNode.have_next())
            if(currentNode.have_next()):
                self.items.append(currentNode)
            else:
                if(self.expand(currentNodeX)):
                    self.items.append(currentNode)

    def expand(self, node):
        nodeID = node.getID()
        nodeRules = node.getRules()

        for rule in nodeRules:
            temp_transition = ''
            temp = []
            dot_moved = False
            haveNext = False
            for i in range(len(rule)):
                if(rule[i] == '.'):
                    if(i < len(rule)-1):
                        if(dot_moved == False):
                            rule[i],rule[i+1] = rule[i+1], rule[i]
                            temp.append(rule)
                            dot_moved = True
                        if(i+1 == len(rule)-1 and rule[i+1] == '.'):
                            haveNext = True
                        next_transition = self.id

            for j in range(len(rule)):
                # get transition input
                if (rule[j] == '.'):
                    temp_transition = rule[j - 1]

                if (rule[j]== '.' and j != len(rule) - 1):
                    if (rule[j + 1] in non_terminal):
                        for rule2 in self.rules:
                            if (rule[j + 1] == rule2[0]):
                                temp_item = []
                                for k in range(len(rule2)):
                                    if (k == 1):
                                        temp_item.append('.')
                                    temp_item.append(rule[k])
                                temp.append(temp_item)

            explored_exist = self.checkExists(self.items, temp)
            unexplored_exist = self.checkExists(self.remaining, temp)
            print(self.currentNode)
            print(node)
            itself = self.checkExists([self.currentNode], temp)
            print(explored_exist)
            print(unexplored_exist)
            print(itself)
            if (explored_exist[0] == False and unexplored_exist[0] == False and itself[0] == False):
                self.createItem(temp, haveNext)
            else:
                if (explored_exist[1] != -1):
                    next_transition = explored_exist[1]
                elif (unexplored_exist[1] != -1):
                    next_transition = unexplored_exist[1]
                elif (itself[1] != -1):
                    next_transition = itself[1]


            print("NT:",next_transition)
            self.transition.append([nodeID, next_transition, temp_transition])

        return True

    def checkExists(self, big_array, temp_state):
        to_item = -1  # not existing lr item
        bigger_is_same = False
        for rules in big_array:
            state = rules.getRules()
            for i in range(len(state)):
                if (len(state) != len(temp_state)):
                    continue
                is_same = True

                for j in range(len(state[i])):
                    if (len(state[i]) != len(temp_state[i])):
                        is_same = False
                        break
                    if (state[i][j] != temp_state[i][j]):
                        is_same = False
                        break

                # print("is same = ", is_same)
                if (is_same == True):
                    to_item = rules.getID()
                    bigger_is_same = True
                else:
                    break

        response = [bigger_is_same, to_item]
        return response

    def viewItems(self):
        for item in self.items:
            print(item.getAll())

    def viewTransitions(self):
        for transition in self.transition:
            print(transition)




def generateParsingTable(non_terminal, terminal, rules):
    ffg = FirstFollowGenerator(non_terminal, terminal, rules)
    lr1 = Itemset_LR1(non_terminal, terminal, rules)
    lr1.viewItems()
    lr1.viewTransitions()

non_terminal = ["S'", "S", "C"]
terminal = ["c", "d"]
rules = [["S'", "S"], ["S", "C", "C"], ["C", "c", "C"], ["C", "d"]]
generateParsingTable(non_terminal,terminal,rules)
