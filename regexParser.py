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

operator_list = ['(', '|', '*', ')']
operator_order = {'(' : 0, '_' : 1, '|' : 2, '*' : 3} #_ is concat

def thompson(n):
    pass

def preprocess_Regex(regex):
    pass

def formatter(list):
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

def parse(regex):
    print(regex)
    regex = change_to_Postfix(regex)
    print(regex)
    regex = ''.join(regex)
    print(regex)
    alphabet = extract_alphabet(regex)
    print(alphabet)

