import datetime
import lr1_parser_generator as lr1

data_test = ""

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


    print(temp_grammar)
    generate_parser()

def generate_parser():
    data_temp = ""
    data = open("temp.txt", 'r')
    for line in data:
        for character in line:
            data_temp = data_temp + character

    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = "58090030_lr1_parser_" + time + ".py"

    automaton_template = "parser_template.py"

    template = open(automaton_template, 'r')
    out_file = open(fileName, 'w')

    data_dump = data_temp
    data_dump = data_dump + '\n\n' + template.read()

    out_file.write(data_dump)
    out_file.close()


if __name__ == '__main__':
    inp = input("Please enter file name (default is sampleGrammar.txt press enter to assign default): ")
    if(inp == ''):
        inp = "sampleGrammar.txt"
    readFile(inp)
    #cdcd$