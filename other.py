def IN(var, question, ram):
    question = question.removeprefix('"').removesuffix('"')
    def generate_range(min_value, max_value):
        min_value = int(min_value, 16) if min_value.isnumeric() else int(min_value, 16)
        max_value = int(max_value, 16) if max_value.isnumeric() else int(max_value, 16)
        result = [hex(i)[2:].upper() for i in range(min_value, max_value + 1)]
        return result

    #print(ram.map)
    var_min = ram.map[var]['min']
    var_max = ram.map[var]['max']
    var_indexes = generate_range(var_min, var_max)
    user_input = input(question)
    if len(user_input)>len(var_indexes):
        user_input = user_input[:len(var_indexes)]

    #for letter in user_input:
    #    pass
    for i in range(len(var_indexes)):
        index = ram.index.index(var_indexes[i])
        try:
            ram.ram[index] = ord(user_input[i])
        except IndexError:
            ram.ram[index] = 0x00


def MSG(format,msg,ram=[]):
    msg = msg.removeprefix('"').removesuffix('"')
    def generate_range(min_value, max_value):
        min_value = int(min_value, 16) if min_value.isnumeric() else int(min_value, 16)
        max_value = int(max_value, 16) if max_value.isnumeric() else int(max_value, 16)
        result = [hex(i)[2:].upper() for i in range(min_value, max_value + 1)]
        return result

    if format == 'T':
        print(msg)

    elif format == 'V':
        var_min = ram.map[msg]['min']
        var_max = ram.map[msg]['max']
        var_indexes = generate_range(var_min,var_max)
        text = ''
        for index in var_indexes:
            index = ram.index.index(index)
            text+=chr(ram.ram[index])
        print(text)

    elif format == 'VR':
        var_min = ram.map[msg]['min']
        var_max = ram.map[msg]['max']
        var_indexes = generate_range(var_min, var_max)
        text_raw = ''
        for index in var_indexes:
            index = ram.index.index(index)
            text_raw += str(hex(ram.ram[index]))[2:]
            text_raw += ' '
        print(text_raw)
    else:
        print(msg)
