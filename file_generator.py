automaton_template = "scanner_template"
main = "main_template"

file1 = open(automaton_template, 'r')
file2 = open(main, 'r')

out_file = open("scanner.py",'w')

data_dump = file1.read()
data_dump = data_dump + '\n\n'
data_dump = data_dump + file2.read()

out_file.write(data_dump)
out_file.close()
