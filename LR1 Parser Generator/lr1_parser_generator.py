import datetime
from lr1_itemset_table_gen import MainLR1gen

def readFile(fileName):
    grammar = open(fileName, 'r')
    temp = ""
    temp_grammar = []
    for line in grammar:
        for character in line:
            if (character != "\n"):
                temp = temp + character
        temp = temp.split()
        temp_grammar.append(temp)
        temp = ""

    #print(temp_grammar)
    non_terminal = temp_grammar[0]
    terminal = temp_grammar[1]
    rules = temp_grammar[2:]
    generate_parser(non_terminal, terminal, rules)

def generate_parser(non_terminal, terminal, rules):
    data_temp = ""
    lr1 = MainLR1gen()

    data = lr1.generateParsingTable(non_terminal, terminal, rules)

    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = "58090030_lr1_parser_" + time + ".py"

    automaton_template = "parser_template.py"

    template = open(automaton_template, 'r')
    out_file = open(fileName, 'w')

    data_dump = "table = " + data
    data_dump = data_dump + '\n\n' + template.read()

    out_file.write(data_dump)
    out_file.close()


if __name__ == '__main__':
    inp = input("Please enter file name (default is sampleGrammar.txt press enter to assign default): ")
    if(inp == ''):
        inp = "sampleGrammar.txt"
    readFile(inp)
    #cdcd$