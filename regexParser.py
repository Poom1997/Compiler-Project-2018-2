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
operator_order = {'(' : 0, '|' : 1, '_' : 2, '*' : 3} #_ is concat

def extract_alphabet(regex):
    alphabet = []
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
    delta_temp = []
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
            delta[currentNode][(currentNode,character)] = {nextNode}
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
            delta[toNode][(toNode,'')] = {fromNode, nextNode}
            delta[currentNode][(currentNode,'')] = {fromNode}
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
            del delta[toNode1]
            for key in elem.keys():
                #print("KEY",key)
                #print("ELIM-KEY ", elem.get(key) - 1)
                temp = key[1]
                #print("TEMP", temp[1])
                delta[fromNode1][(fromNode1, temp)] = {int(list(elem.get(key))[0]) - 1}
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
            delta[toNode1][(toNode1,'')] = {nextNode}
            delta[toNode2][(toNode2,'')] = {nextNode}
            if startNode == fromNode1 or startNode == fromNode2:
                startNode = currentNode
            if acceptNode == toNode2 or acceptNode == toNode1:
                acceptNode = nextNode
            #print(delta)

    temp = []
    for element in delta:
        if(element == {}):
            temp.append(element)
            delta_temp.append(temp)
            temp = []
        else:
            temp.append(element)

    #print(delta)
    iteration = 0
    if(len(delta_temp)> 1):
        for each_set in delta_temp:
            iteration += 1
            if(iteration == len(delta_temp)):
                break
            else:
                #print(each_set)
                next_start = delta_temp[iteration][-2]
                next_start_key = list(next_start.keys())[0]
                next_start_values = list(next_start.values())[0]
                this_start = each_set[-2]
                this_start_key = list(this_start.keys())[0]
                this_start_values = list(this_start.values())[0]
                #print(this_start_values)
                this_begin = each_set[0]
                this_begin_key = list(this_begin.keys())[0]

                #print(next_start)
                #print(next_start_key[0])
                #print(next_start_values)
                #print(this_start_key[0])
                #print(this_start_values)
                #print(list(this_start_values)[0])
                this_end = {(list(this_start_key)[0]+1, '') : {next_start_key[0]}}
                each_set[-1] = this_end

                next_start_values.add(this_begin_key[0])
                next_start[next_start_key] = next_start_values
                startNode = next_start_key[0]
                acceptNode = next_start_key[0]+1


    delta = delta_temp

    return delta, startNode, acceptNode

def formatter(name, delta, start, accept, alphabet):
    #Get Q
    Q = ''
    for i in range(0,accept+1):
        Q = Q + str(i) + ','
    Q = '{' + Q[:-1] + '}'
    print("Q: ", Q)

    #get Sigma
    Sigma = set(alphabet)
    temp = ''
    for i in Sigma:
        temp = temp + "'" + str(i) + "',"
    Sigma = '{' + temp[:-1] +'}'
    print("Sigma: ", Sigma)

    #getDelta
    temp = '{'
    for each_set in delta:
        for each_pair in each_set:
            temp = temp + str(each_pair)[1:-1] + ','

    temp = temp[:-2] + '}'
    delta = temp
    print("Delta: ", delta)

    #get q0
    q0 = str(start)
    print("q0: ", start)

    #get F
    F = '{' + str(accept) + '}'
    print("F: ", F)

    #get Name
    name = str(name)
    print("Name: ", name)

    output_string = '['+ Q + ',' + Sigma + ',' + delta + ',' + q0 + ',' + F + ',"' + name + '"]'
    print(output_string)

    return output_string

def parse(name, regex, regexList):
    #print(regex)
    regex = change_to_Postfix(regex)
    #print(regex)
    regex = ''.join(regex)
    #print(regex)

    alphabet = extract_alphabet(regex)
    #print(alphabet)
    delta, startNode, acceptNode = thompson(regex, alphabet)
    #print(delta, startNode, acceptNode, alphabet_all)
    alphabet_all = []
    if(regexList is not None):
        for each_regex in regexList:
            for items in extract_alphabet(each_regex[1]):
                alphabet_all.append(items)
        #print(alphabet_all)
        output_string = formatter(name, delta, startNode, acceptNode, alphabet_all)
    else:
        output_string = formatter(name, delta, startNode, acceptNode, alphabet)

    return output_string

