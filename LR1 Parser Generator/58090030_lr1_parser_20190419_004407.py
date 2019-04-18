table = {0:{"c": ("s",3),"d": ("s",4),"S": ("", 1),"C": ("", 2),"S'": ("", "accept")},1:{"$": ("r", ("S'", ("S")))},2:{"c": ("s", 3),"d": ("s", 4),"C": ("", 5)},3:{"c": ("s", 3),"d": ("s", 4),"C": ("", 6)},4:{"c": ("r", ("C",("d"))),"d": ("r", ("C",("d"))),"$": ("r", ("C",("d")))},5:{"$": ("r", ("S",("C","C")))},6:{"c": ("r", ("C",("c","C"))),"d": ("r", ("C",("c","C"))),"$": ("r", ("C",("c","C")))}}


def parse(input_string):
    stack = ['$',0]
    input_string = input_string + '$'
    input_index = 0

    start_symbol = "S'"
    while stack[-1] != 'accept':
        #print(stack)
        current_state = stack[-1]
        if input_string[input_index] not in table[current_state]:
            # reject the string
            print('String ' + input_string[:-1] + ' Rejected!')
            break
        action, goto = table[current_state][input_string[input_index]]
        if action == 's':
            stack.append(input_string[input_index])
            stack.append(goto)
            input_index += 1
        elif action == 'r':
            new_symbol, RHS = goto
            for item in RHS:
                stack.pop() # state number
                stack.pop() # symbol
            stack.append(new_symbol)
            if new_symbol not in table[stack[-2]]:
                # reject the string
                print('String ' + input_string[:-1] + ' Rejected!')
                break
            _, goto = table[stack[-2]][new_symbol]
            stack.append(goto)    
    if stack[-1] == 'accept':
        print('String ' + input_string[:-1] + ' Accepted!')
	
if __name__ == '__main__':
    print()
    while(True):
        inp = input("Please enter string to parse: ")
        print()
        parse(inp)
        print()
