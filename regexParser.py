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

def thompson_or(n):
    pass

def formatter(list):
    print(list)

def parse(regex):
    stack = Stack()
    regex = '(' + regex + ')'

    iteration = 0
    and_count = 0
    depth = -1
    main_depth = 0

    main_list = []
    temp_list = []

    for character in regex:
        iteration += 1

        if(character == '('):
            stack.push(character)
            stack.add_Start(iteration)
            temp_list.append([])
            depth += 1

        elif(character == "|"):
            temp = []
            for i in range(0, and_count):
                temp.append(stack.pop())
            if(depth!=0):
                temp_list[depth].append(temp[::-1])
            else:
                main_list.append(temp[::-1])
                main_depth += 1
            and_count = 0

        elif(character == ")"):
            temp = []
            for i in range(0, and_count):
                temp.append(stack.pop())
                #print("TMP ", temp)
            #print("TMP ", temp)
            if(len(temp)>0):
                if(depth != 0):
                    #print(depth)
                    temp_list[depth].append(temp[::-1])
                    depth -= 1
                    #print("TL", temp_list)
                    and_count = 0
                    stack.pop()
                    #print("LS", len(temp_list))
                    #print(main_list)
                    #print(main_depth)
                    if(main_depth == 0):
                        main_list.append(temp_list.pop())
                    else:
                        main_list[main_depth].append(temp_list.pop())
                    #print(main_list)
                else:
                    if(main_depth == 0):
                        main_list.append(temp.pop())
                    else:
                        main_list[main_depth].append(temp.pop())
                    main_depth += 1

        else:
            and_count += 1
            stack.push(character)

        #print(iteration)
        #stack.print_value()
    print(main_list)

    #print("TMP: " , temp_list)
    #stack.print_Start()


    for each_element in main_list:
        formatter(each_element)

