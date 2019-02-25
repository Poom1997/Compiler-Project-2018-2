class Stack:
    def __init__(self):
        self.data = []
        self.currentPos = 0
        self.start = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def print_value(self):
        print(self.data)

    def previous(self):
        return self.data[-1]

    def empty(self):
        if(len(self.data) == 0):
            return True
        else:
            return False

operator_list = ['(', '|', '*', ')', '_']
operator_order = {'(' : 0, '_' : 1, '|' : 2, '*' : 3} #_ is concat

def preprocess_Regex(regex):
    pass

def extract_alphabet(regex):
    alphabet = ['']
    for character in regex:
        if(character in operator_list):
            pass
        else:
            alphabet.append(character)

    return alphabet

def change_to_Postfix(regex):
    stack = Stack()
    output = []
    for character in regex:
        #print(character)
        #stack.print_value()
        if(character not in operator_list):
            output.append(character)

        elif(character == '('):
            stack.push(character)

        elif(character == ')'):
            temp = stack.pop()
            while(temp != '('):
                output.append(temp)
                temp = stack.pop()

        else:
            while(not stack.empty() and (operator_order[stack.previous()] >= operator_order[character])):
                output.append(stack.pop())
            stack.push(character)

    while(not stack.empty()):
        temp = stack.pop()
        output.append(temp)

    return output

def thompson(regex, alphabet):
    delta = []
    stack = Stack()

    startNode = 0
    acceptNode = 1
    cnt = -1

    for character in regex:
        if character in alphabet:
            cnt = cnt + 1
            currentNode = cnt
            cnt = cnt + 1
            nextNode = cnt
            delta.append({})
            delta.append({})
            stack.push([currentNode, nextNode])
            #stack.print_value()
            delta[currentNode][(currentNode,character)] = nextNode
            #print(delta)

        elif character == '*':
            fromNode, toNode = stack.pop()
            cnt = cnt + 1
            currentNode = cnt
            cnt = cnt + 1
            nextNode = cnt
            delta.append({})
            delta.append({})
            stack.push([currentNode, nextNode])
            delta[toNode][(currentNode,'')] = {fromNode, nextNode}
            delta[currentNode][(currentNode,'')] = {fromNode, nextNode}
            if startNode == fromNode:
                startNode = currentNode
            if acceptNode == toNode:
                acceptNode = nextNode
            #print(delta)

        elif character == '_':
            fromNode1, toNode1 = stack.pop()
            fromNode2, toNode2 = stack.pop()
            toNode1 = fromNode1
            fromNode1 = toNode2
            stack.push([fromNode2, toNode1])
            elem = delta[toNode1]
            delta.remove(elem)
            for key in elem.keys():
                delta[fromNode1][key] = elem.get(key) - 1
            cnt = cnt - 1
            if startNode == fromNode1:
                startNode = fromNode2
            if acceptNode == toNode2:
                acceptNode = toNode1
            #print(delta)

        else:
            cnt = cnt + 1
            currentNode = cnt
            cnt = cnt + 1
            nextNode = cnt
            delta.append({})
            delta.append({})
            fromNode1, toNode1 = stack.pop()
            fromNode2, toNode2 = stack.pop()
            stack.push([currentNode, nextNode])
            delta[currentNode][(currentNode,'')] = {fromNode2, fromNode1}
            delta[toNode1][(toNode1,'')] = nextNode
            delta[toNode2][(toNode2,'')] = nextNode
            if startNode == fromNode1 or startNode == fromNode2:
                startNode = currentNode
            if acceptNode == toNode2 or acceptNode == toNode1:
                acceptNode = nextNode
            #print(delta)

    for element in delta:
        print(element)

    return delta, startNode, acceptNode

def formatter(list):
   pass


def parse(regex):
    #print(regex)
    regex = change_to_Postfix(regex)
    #print(regex)
    regex = ''.join(regex)
    #print(regex)
    alphabet = extract_alphabet(regex)
    #print(alphabet)
    automaton = thompson(regex, alphabet)
    print(automaton)

