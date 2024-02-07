class SimpleMem:
    def __init__(self):
        self.ram = [0x00]*65535
        self.index = []
        self.used = ['0', 'A', '12']
        self.map = {}
        for i in range(len(self.ram)+1):
            index_nr = str(hex(i))[2:]
            self.index.append(index_nr.upper())
