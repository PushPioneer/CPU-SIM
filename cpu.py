import mem
import core
ram = mem.SimpleMem()

#casm = '''PUSH 0xA 0
#DMPADDR 0
#test_var DD
#IN test_var "name: "
#MSG T "Hallo: "
#MSG V test_var
#MSG T "TEST"
#HLD'''
with open('code.casm','r') as f:
    casm = f.read()
    f.close()
def split_string_except_inside_quotes(input_string):
    inside_quotes = False
    result_list = []
    current_word = ''

    for char in input_string:
        if char == '"':
            inside_quotes = not inside_quotes
            current_word += char
        elif char == ' ' and not inside_quotes:
            if current_word:
                result_list.append(current_word)
                current_word = ''
        else:
            current_word += char

    if current_word:
        result_list.append(current_word)

    return result_list

for instruction in casm.split('\n'):

    if instruction.__contains__(','):
        instruction = instruction.replace(',', ' ')

    line = split_string_except_inside_quotes(instruction)

    if len(line) == 0:
        pass
    else:

        if len(line) < 4:
            rn = len(line)
            tb = 4 - rn
            for i in range(tb):
                line.append('')
        core.execute(key=line[0],op1=line[1],op2=line[2],op3=line[3])
