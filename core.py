import alu
import logic
import mem
import other
import ram_var_man
import gpu
import time

gpu = gpu.SimpleGpu()
ram = mem.SimpleMem()

gpu.boot()

def execute(key, op1, op2, op3):
    opperants = key,op1,op2,op3
    xopperants = []
    for operation in opperants:
        if operation == '' or operation == ' ':
            pass
        else:
            xopperants.append(operation)
    xopperants.remove(key)
    if key == 'INC':
        alu.INC(ram=ram,*xopperants)
    elif key == 'DEC':
        alu.DEC(ram=ram,*xopperants)
    elif key == 'ADD':
        alu.ADD(ram=ram, *xopperants)
    elif key == 'SUB':
        alu.SUB(ram=ram, *xopperants)
    elif key == 'AND':
        logic.AND(ram=ram, *xopperants)
    elif key == 'OR':
        logic.OR(ram=ram, *xopperants)
    elif key == 'XOR':
        logic.XOR(ram=ram, *xopperants)
    elif key == 'MSG':
        gpu.show_text2(text=op2,ram=ram,format=op1)
        #other.MSG(ram=ram, *xopperants)
    elif key == 'PUSH':
        ram_var_man.PUSH(ram=ram, *xopperants)
    elif key == 'POP':
        ram_var_man.POP(ram=ram, *xopperants)
    elif key == 'MOV':
        ram_var_man.MOV(ram=ram, *xopperants)
    elif key == 'IN':
        gpu.IN(ram=ram,question=op2,var=op1)
        #other.IN(ram=ram, *xopperants)
    elif key == 'BS':
        logic.BS(ram=ram, *xopperants)
    elif key == 'NOT':
        logic.NOT(ram=ram, *xopperants)
    elif key == 'DMPADDR':
        ram_var_man.DMPADDR(ram=ram, *xopperants)
    elif key == 'DMPMEM':
        ram_var_man.DMP(ram=ram)
    elif key == 'DSPPRN':
        gpu.show_text(op1)
    elif key == 'SLEEP':
        time.sleep(float(op1))
    elif key == 'HLD':
        input()
    elif op1 in ['DB','DW','DD','DQ','DT']:
        if op2 == '':
            ram_var_man.MALLOC(size=op1,name=key,ram=ram)
        else:
            ram_var_man.VARMAN(ram=ram,*xopperants)
    elif op1.isnumeric():
        ram_var_man.MALLOC(ram=ram, name=key,size=int(op1))
    else:
        pass
