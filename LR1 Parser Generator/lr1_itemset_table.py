from first_follow_generator import FirstFollowGenerator

import copy
class Item:
    def __init__(self, rules, id_inp, next, lookahead = '$'):
        self.rules = rules
        self.id = id_inp
        self.end = next
        self.lookahead = lookahead

    def have_next(self):
        return self.end

    def getLookahead(self):
        return self.lookahead

    def have_next(self):
        return self.end

    def getID(self):
        return self.id

    def getRules(self):
        return self.rules

    def getAll(self):
        print("S " + str(self.id), end = " : ")
        print("Have_Next = " + str(self.end), end = " : ")
        print("Rules = " + str(self.rules))


class Itemset_LR1:
    def __init__(self, non_terminal, terminal, rules, ff):
        self.non_terminal = non_terminal
        self.terminal = terminal
        self.rules = rules
        self.items = []
        self.remaining = []
        self.transition = []
        self.currentNode = []
        self.id = 0
        self.first_follow = ff
        self.init_states()
        self.expand_All_Items()


    def createItem(self, rule, next, lookahead):
        temp_item = Item(rule, self.id, next, lookahead)
        self.remaining.append(temp_item)
        self.id = self.id + 1
       # print(rule)

    def init_states(self):
        temp_deep = copy.deepcopy(self.rules)
        temp = [temp_deep[0]]
        temp[0].insert(1, '.')
        start = temp[0]
        lookahead = temp[0][2]
        print(lookahead)
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

        first_of_lookahead = self.first_follow.get_first_of(lookahead)
        self.createItem(temp, False, first_of_lookahead)

    def expand_All_Items(self):
        #print(len(self.remaining))
        #i = 0
        while(len(self.remaining) != 0):
            #for item in self.items:
                #item.getAll()
                #pass
            currentNode = self.remaining.pop(0)
            currentNodeX = copy.deepcopy(currentNode)
            self.currentNode = copy.deepcopy(currentNode)
            if(currentNode.have_next()):
                self.items.append(currentNode)
            else:
                if(self.expand(currentNodeX)):
                    self.items.append(currentNode)
            #if(i == 2):
                #break
            #i += 1
            #currentNode.getAll()
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
                                    temp_item.append(rule2[k])
                                temp.append(temp_item)

            explored_exist = self.checkExists(self.items, temp)
            unexplored_exist = self.checkExists(self.remaining, temp)
            #print(self.currentNode)
            #print(node)
            itself = self.checkExists([self.currentNode], temp)
            #print(explored_exist)
            #print(unexplored_exist)
            #print(itself)

            if (explored_exist[0] == False and unexplored_exist[0] == False and itself[0] == False):
                self.createItem(temp, haveNext, self.first_follow.get_first_of(temp[0]))
            else:
                if (explored_exist[1] != -1):
                    next_transition = explored_exist[1]
                elif (unexplored_exist[1] != -1):
                    next_transition = unexplored_exist[1]
                elif (itself[1] != -1):
                    next_transition = itself[1]

            #print("NT:",next_transition)
            self.transition.append([nodeID, temp_transition, next_transition])

        return True

    def checkExists(self, input_rules, temp_rule):
        next_transition = -1
        temp = False
        for rules in input_rules:
            rule = rules.getRules()
            lookahead = rules.getLookahead()
            for i in range(len(rule)):
                if (len(rule) != len(temp_rule)):
                    continue
                is_same = True

                for j in range(len(rule[i])):
                    if (len(rule[i]) != len(temp_rule[i]) or rule[i][j] != temp_rule[i][j]):
                        is_same = False
                        break

                if (is_same == True):
                    next_transition = rules.getID()
                    temp = True
                else:
                    break
        return (temp, next_transition)

    def getRules(self):
        return self.rules

    def getID(self):
        return self.id

    def getItems(self):
        return self.items

    def getTransitions(self):
        return self.transition

    def viewItems(self):
        for item in self.items:
            item.getAll()

    def viewTransitions(self):
        for transition in self.transition:
            print(transition)

class ParsingTable:
    def __init__(self, rules, transition, id, first, follow):
        self.rules = rules
        self.transition = transition
        self.num = id
        self.first = first
        self.follow = follow

def generateParsingTable(non_terminal, terminal, rules):
    ff = FirstFollowGenerator(non_terminal, terminal, rules)
    lr1 = Itemset_LR1(non_terminal, terminal, rules, ff)
    lr1.viewItems()
    lr1.viewTransitions()
    print(lr1.getRules())
    print(lr1.getID())


non_terminal = ["S'", "S", "C"]
terminal = ["c", "d"]
rules = [["S'", "S"], ["S", "C", "C"], ["C", "c", "C"], ["C", "d"]]
generateParsingTable(non_terminal,terminal,rules)
