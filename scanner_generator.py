import datetime

def thomson_algorithm(regex):
    pass

def generate_scanner(regex):
    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fileName = "58090030_scanner_" + time+".py"

    automaton_template = "scanner_template.py"

    template = open(automaton_template, 'r')
    out_file = open(fileName,'w')

    data_dump = regex
    data_dump = data_dump + '\n\n' + template.read()

    out_file.write(data_dump)
    out_file.close()

if __name__ == '__main__':
    regex = "regex_list = [[{0,1,2,3},{'a','b'},{(0, 'a'): {0},(0, 'b'): {1},(1, 'a'): {2},(2, 'b'): {3}},0,{3},'a*bab'],[{0, 1, 2},{'a', 'c'},{(0, 'a'): {1},(1, 'c'): {2},(2, ''): {0}},0,{2},'(ac)*']]"
    generate_scanner(regex)