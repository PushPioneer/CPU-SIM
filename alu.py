def INC(addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = ram.ram[index] + 1
    print(ram.ram[index])

def DEC(addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = ram.ram[index] - 1
    print(ram.ram[index])

def ADD(op1,op2,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = op1 + op2

def SUB(op1,op2,addr,ram):
    index = ram.index.index(addr)
    ram.ram[index] = op1 - op2

