def IS_NULL(addr,ram):
    index = ram.index.index(addr)
    if ram.ram[index] == 0:
        return True
    return False

def MALLOC(name,size,ram):
    if size == 'DB': #1byte
        size = 1
    elif size == 'DW':#2byte
        size = 2
    elif size == 'DD':#4byte
        size = 4
    elif size == 'DQ':#8byte
        size = 8
    elif size == 'DT':#10byte
        size = 10
    size_counter = 0
    reserved = []
    for addr in ram.index:
        if addr in ram.used:
            #print('passed: ', addr)
            size_counter = 0
            reserved = []
        else:
            size_counter+=1
            reserved.append(addr)

            if size_counter == size:
                for addr in reserved:
                    ram.used.append(addr)
                var_to_map = {name:{"min":min(reserved),"max":max(reserved)}}
                ram.map.update(var_to_map)
                #print(ram.map)
                return ram.map, reserved



def VARMAN(name,type,data,ram,allocator=MALLOC):
    if type == 'DB': #1byte
        size = 1
    elif type == 'DW':#2byte
        size = 2
    elif type == 'DD':#4byte
        size = 4
    elif type == 'DQ':#8byte
        size = 8
    elif type == 'DT':#10byte
        size = 10
    else: #custom
        size = int(type)
        if size < len(data):
            size = len(data)
            #print('set lenght to', size)

    useless, allocated = allocator(size, name, ram)
    counter = 0
    for alloc_addr in allocated:
        index = ram.index.index(alloc_addr)
        try:
            ram.ram[index] = ord(data[counter])
        except:
            ram.ram[index] = 0x00
        counter+=1

def PUSH(src,dst,ram):
    if src.startswith('0x'):
        src_data = int(src,16)
        dst_index = ram.index.index(dst)
        ram.ram[dst_index] = src_data
    else:
        src_index = ram.index.index(src)
        dst_index = ram.index.index(dst)
        src_data = ram.ram[src_index]
        ram.ram[dst_index] = src_data
        ram.ram[src_index] = 0x00

def POP(addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = 0x00

def MOV(src,dst,ram):
    src_index = ram.index.index(src)
    dst_index = ram.index.index(dst)
    src_data = ram.ram[src_index]
    ram.ram[dst_index] = src_data

def DMP(ram):
    print(ram.ram)

def DMPADDR(addr,ram):
    index = ram.index.index(addr)
    print(ram.ram[index])