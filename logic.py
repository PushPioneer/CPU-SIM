def AND(op1,op2,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = op1&op2

def OR(op1,op2,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = op1|op2

def XOR(op1,op2,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = op1^op2

def NOT(op,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = ~op

def BS(val,op,shift,addr,ram):
    if op == '<<<':
        index = ram.index.index(addr)
        ram.ram[index] = val<<shift
    elif op == '>>>':
        index = ram.index.index(addr)
        ram.ram[index] = val >> shift
