class Stack:
    def __init__(self):
        self.data = []
        self.currentPos = 0
        self.start = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def add_Start(self, value):
        self.start.append(value)

    def print_Start(self):
        print(self.start)

    def set_CurrentPos(self, value):
        self.currentPos = value

    def print_value(self):
        print(self.data)

def formatter(list):
    #print("LST " , list)
    for each_element in list:
        if(len(each_element) == 1):
            #print("EE ", each_element)
            print(each_element[0], end = " ")
        else:
            formatter(each_element)
    return 0

def parse(regex):
    stack = Stack()
    regex = '(' + regex + ')'

    iteration = 0
    and_count = 0
    depth = -1

    main_list = []
    temp_list = []
    temp_and_list = []
    element_id = -1

    for character in regex:
        iteration += 1
        if(character == '('):
            stack.push(character)
            stack.add_Start(iteration)
            temp_list.append([])
            depth += 1
            #print(depth)

        elif(character == "|"):
            temp = []
            for i in range(0, and_count):
                temp.append(stack.pop())
            temp_list[depth].append(temp[::-1])
            and_count = 0

        elif(character == ")"):
            temp = []
            for i in range(0, and_count):
                temp.append(stack.pop())
            temp_list[depth].append(temp[::-1])
            and_count = 0
            stack.pop()
            #print("LS", len(temp_list))
            #print("TL", temp_list)
            main_list.append(temp_list.pop())
            depth -= 1

        else:
            and_count += 1
            stack.push(character)

        #print(iteration)
        #stack.print_value()

    #print("TMP: " , temp_list)
    #stack.print_Start()
    #print(main_list)

    for each_element in main_list:
        formatter(each_element)
