#File I/O for getting the machine code as a list of str
def file_handling(file_name:str):
    f = open(file_name, 'r')
    machine_code = []
    for line in f.readlines():
        machine_code.append(line.rstrip(" ")[: -1])#to remove 0x and \n characters
    f.close()
    #print(machine_code)
    return machine_code #returns list of instructions in hexadecimal

#initialising an instruction memory for usage
def create_instruction_memory():
    hexadecimal_str = "00400000"
    addresses = []
    while hexadecimal_str != "00402400":
        hexadecimal_str = bin(int(hexadecimal_str, 16))[2:].zfill(32)
        addresses.append(hexadecimal_str)
        nextpc = str(bin(int(hexadecimal_str, 2) + int('4', 16)))[2:].zfill(32)
        hexadecimal_str = str(hex(int(nextpc, 2))[2:].zfill(8))
    return dict(zip(addresses, [' ' for _ in range(len(addresses))]))#create a dictionary with keys from 00040000 to 00040240 in binary

#initialising register file 
def create_register_file():
    register_no = []
    start = "00000"
    while start != "100000":
        register_no.append(start)
        if start == "11111":
            break
        start = bin(int(start, 2) + int("00001", 2))[2:].zfill(5)
    return dict(zip(register_no, [''.join(['0' for _ in range(32)])] + [' ' for i in range(len(register_no) - 1)])) #create a dictionary with keys from 00000 to 11111

#initialising data memory
'''
def create_data_memory():
    start = bin(int("10010000", 16))[2:].zfill(32)
    data = []
    while start != bin(int("1001015c", 16))[2:].zfill(32):
        data.append(start)
        start = bin(int(start, 2) + int("0100", 2))[2:].zfill(32)
    return dict(zip(data, [' ' for i in range(len(data))]))#create a dictionary with keys from 10010000 to 1001015c
'''
def create_data_memory():
    hexadecimal_str = "10000000"
    addresses = []
    while hexadecimal_str != "100101bc":
        hexadecimal_str = bin(int(hexadecimal_str, 16))[2:].zfill(32)
        addresses.append(hexadecimal_str)
        nextpc = str(bin(int(hexadecimal_str, 2) + int('4', 16)))[2:].zfill(32)
        hexadecimal_str = str(hex(int(nextpc, 2))[2:].zfill(8))
    return dict(zip(addresses, [' ' for _ in range(len(addresses))]))#create a dictionary with keys from 00040000 to 00040240 in binary
#helpers
register_file = create_register_file()
register_file["lo"] = ' '
data_memory = create_data_memory()
instruction_memory = create_instruction_memory()
register_file[bin(int("29", 10))[2:].zfill(5)] = "1111111111111111111111111111100"

#adding the machine code to the instruction memory
def add_to_memory(file_name, code):
    machine_code = file_handling(file_name)
    j = 0
    if code == 'S':
        start = list(instruction_memory.keys()).index(bin(int("0040004c", 16))[2:].zfill(32))
    else:
        start = list(instruction_memory.keys()).index(bin(int("0040008c", 16))[2:].zfill(32))
    for i in list(instruction_memory.keys())[start:]:
            if j >= len(machine_code):
                return instruction_memory
            instruction_memory[i] = machine_code[j]
            j += 1
    return instruction_memory

#Taking input for respective code
def input_function():
    name = None
    g = input("Enter type of code: ")
    if g == "S":
        name = "dumpsorting.txt"
        n = int(input("Enter length of array: "))
        inp_add = int(input("Enter input address: "))
        register_file[bin(int("9", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("10", 10))[2:].zfill(5)] = bin(inp_add)[2:].zfill(32)
        #print(register_file)
        start_add = register_file[bin(int("10", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        out_add = int(input("Enter output address: "))
        register_file[bin(int("11", 10))[2:].zfill(5)] = bin(out_add)[2:].zfill(32)

    elif g == "C":
        name = "dumpconvolution.txt"
        n = int(input("Enter length of x: "))
        inp_add = int(input("Enter the x input address: "))
        register_file[bin(int("9", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("10", 10))[2:].zfill(5)] = bin(inp_add)[2:].zfill(32)
        #print(register_file)
        start_add = register_file[bin(int("10", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        n = int(input("Enter length of h: "))
        inp_add = int(input("Enter h input address: "))
        register_file[bin(int("11", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("13", 10))[2:].zfill(5)] = bin(inp_add)[2:].zfill(32)
        #print(register_file)
        start_add = register_file[bin(int("13", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        out_add = int(input("Enter output address: "))
        register_file[bin(int("14", 10))[2:].zfill(5)] = bin(out_add)[2:].zfill(32)

    elif g == "M":
        name = "dumpedhexmatrix.txt"
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))
        p = int(input("Enter p: "))
        if n != p:
            print("Matrix Multiplication not possible")
            return
        q = int(input("Enter q: "))
        register_file[bin(int("9", 10))[2:].zfill(5)] = bin(m)[2:].zfill(32)
        register_file[bin(int("17", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("18", 10))[2:].zfill(5)] = bin(q)[2:].zfill(32)
        x1_add = int(input("Enter first matrix input address: "))
        register_file[bin(int("10", 10))[2:].zfill(5)] = bin(x1_add)[2:].zfill(32)
        start_add = register_file[bin(int("10", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n*m):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)

        x2_add = int(input("Enter second matrix input address: "))
        register_file[bin(int("13", 10))[2:].zfill(5)] = bin(x2_add)[2:].zfill(32)
        start_add = register_file[bin(int("10", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n*q):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        y_add = int(input("Enter output address: "))
        register_file[bin(int("14", 10))[2:].zfill(5)] = bin(y_add)[2:].zfill(32)
    else:
        name = "machinec.txt"
        n = int(input("Enter length of x: "))
        inp_add = int(input("Enter the x input address: "))
        register_file[bin(int("9", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("10", 10))[2:].zfill(5)] = bin(inp_add)[2:].zfill(32)
        #print(register_file)
        start_add = register_file[bin(int("10", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        n = int(input("Enter length of h: "))
        inp_add = int(input("Enter h input address: "))
        register_file[bin(int("11", 10))[2:].zfill(5)] = bin(n)[2:].zfill(32)
        register_file[bin(int("13", 10))[2:].zfill(5)] = bin(inp_add)[2:].zfill(32)
        #print(register_file)
        start_add = register_file[bin(int("13", 10))[2:].zfill(5)]
        #print(start_add)
        for i in range(n):
            x = int(input())
            data_memory[start_add] = bin(int(str(x), 10))[2:].zfill(32)
            #print(data_memory[start_add])
            start_add = bin(int(str(start_add), 2) + int("100", 2))[2:].zfill(32)
            #print(start_add)
        out_add = int(input("Enter output address: "))
        register_file[bin(int("14", 10))[2:].zfill(5)] = bin(out_add)[2:].zfill(32)
    #print(name)
    add_to_memory(name, g)
    return g

def create_stack_memory():
    hexadecimal_str = "7ffffffc"
    addresses = []
    while hexadecimal_str != "7fffffe4":
        hexadecimal_str = bin(int(hexadecimal_str, 16))[2:].zfill(32)
        addresses.append(hexadecimal_str)
        nextpc = str(bin(int(hexadecimal_str, 2) + int('-4', 16)))[2:].zfill(32)
        hexadecimal_str = str(hex(int(nextpc, 2))[2:].zfill(8))
    return dict(zip(addresses, [' ' for _ in range(len(addresses))]))#create a dictionary with keys from 00040000 to 00040240 in binary

stack_memory = create_stack_memory()

#helpers
r_format = ['000000']
i_format = ["100011", "101011", "000100", "001000", "001010", "000101", "111111", "001010"]
j_format = ["000010"]
code = input_function()

func_ALU = {"100000":"0010", "100010":"0110", "100100":"0000", "100101":"0001", "101010":"0111", "000000":"0100", "011000":"0101", "010010":"1000"}
lw = "100011"
sw = "101011"
beq = "000100"
bne = "000101"
addi = "001000"
subi = "111111"
slti = "001010"

#Instruction class to denote one particular instruction
class Instruction:
    #initialisation
    def __init__(self, pc):
        self.pc = pc
        self.nextpc = str(str(bin(int(pc, 2) + int('4', 16))))[2:].zfill(32)
        self.opcode = "0"
        self.machine_code = ["0"]
        self.rs = "0"
        self.rt = "0"
        self.rd = "0"
        self.shamt = "0"
        self.funct = "0"
        self.imm = "0"
        self.address = "0"
        self.ALUOp = "0"
        self.ALUa = "0"
        self.ALUb = "0"
        self.ALUc = "0"
        self.ALUout = "0"
        self.ALUSrc = "0"
        self.branch = "0"
        self.regWrite = "0"
        self.regDst = "0"
        self.memWrite = "0"
        self.memToreg = "0"
        self.memRead = "0"
        self.jump = "0"
        self.readData1 = "0"
        self.readData2 = "0"
        self.memReadp = "0"
        self.add = "0"
        self.write = "0"
        self.writeData = "0"
        self.format = 'n'
    
    #Instruction fetch - retrieves instruction from instruction memory
    def fetch(self, pc):
        if instruction_memory[self.pc] == '' or instruction_memory[self.pc] == ' ':
            return
        print(instruction_memory[self.pc])
        self.machine_code = bin(int(instruction_memory[self.pc], 16))[2:].zfill(32)

    #splits the machine code based on the format of instruction
    def main_decoder_unit(self, machine_code, opcode):
        if self.opcode == "000000":
            self.rs = bin(int(machine_code[6:11], 2))[2:].zfill(5)
            self.rt = bin(int(machine_code[11:16], 2))[2:].zfill(5)
            self.rd = bin(int(machine_code[16:21], 2))[2:].zfill(5)
            self.shamt = bin(int(machine_code[21:26], 2))[2:].zfill(5)
            self.funct = bin(int(machine_code[26:], 2))[2:].zfill(6)
            return 'r'
        elif self.opcode in i_format:
            self.rs = bin(int(machine_code[6:11], 2))[2:].zfill(5)
            self.rt = bin(int(machine_code[11:16], 2))[2:].zfill(5)
            self.imm = bin(int(machine_code[16:], 2))[2:].zfill(16)
            return 'i'
        elif self.opcode in j_format:
            self.address = bin(int(machine_code[6:], 2))[2:].zfill(26)
            return 'j'

    #generate ALU control signals
    def generate_ALU_control(self):
        if self.ALUOp == "00":
            self.ALUc = "0010"
        elif self.ALUOp == "01":
            self.ALUc = "0110"
        elif self.ALUOp == "10":
            self.ALUc = func_ALU[self.funct]
        elif self.ALUOp == "11":
            self.ALUc = "0111"

    #generate all the control signals - main signals + ALU control signals
    def generate_control_signals(self, format):
        if format == 'r':
            self.regWrite = 1
            self.regDst = 1
            self.ALUSrc = 0
            self.branch = "00"
            self.memWrite = 0
            self.memToreg = 0
            self.memRead = 0
            self.ALUOp = "10"
            self.jump = 0
        elif format == 'i':
            if self.opcode == lw:
                self.regWrite = 1
                self.regDst = 0
                self.ALUSrc = 1
                self.branch = "00"
                self.memWrite = 0
                self.memToreg = 1
                self.ALUOp = "00"
                self.memRead = 1
                self.jump = 0
            elif self.opcode == sw:
                self.regWrite = 0
                self.regDst = 0
                self.ALUSrc = 1
                self.branch = "00"
                self.memWrite = 1
                self.memRead = 0
                self.memToreg = 0
                self.ALUOp = "00"
                self.jump = 0
            elif self.opcode == beq or self.opcode == bne:
                self.regWrite = 0
                self.regDst = 0
                self.ALUSrc = 0
                if self.opcode == beq:
                    self.branch = "01"
                else:
                    self.branch = "10"
                self.memWrite = 0
                self.memToreg = 0
                self.memRead = 0
                self.ALUOp = "01"
                self.jump = 0
            elif self.opcode == addi:
                self.regWrite = 1
                self.regDst = 0
                self.ALUSrc = 1
                self.branch = "00"
                self.memWrite = 0
                self.memRead = 0
                self.memToreg = 0
                self.ALUOp = "00"
                self.jump = 0
            elif self.opcode == subi:
                self.regWrite = 1
                self.regDst = 0
                self.ALUSrc = 1
                self.branch = "00"
                self.memWrite = 0
                self.memRead = 0
                self.memToreg = 0
                self.ALUOp = "01"
                self.jump = 0
            elif self.opcode == slti:
                self.regWrite = 1
                self.regDst = 0
                self.ALUSrc = 1
                self.branch = "00"
                self.memWrite = 0
                self.memRead = 0
                self.memToreg = 0
                self.ALUOp = "11"
                self.jump = 0
        elif self.opcode in j_format:
            self.regWrite = 0
            self.regDst = 0
            self.ALUSrc = 0
            self.branch = "00"
            self.memWrite = 0
            self.memRead = 0
            self.memToreg = 0
            self.ALUOp = "00"
            self.jump = 1
        self.generate_ALU_control()

    #sign extend immediate field
    def sign_extend(self, format, imm):
        if format == "i":
            if imm[0] == "1":
                extend = ''.join(["1" for i in range(16)])
                return str(extend) + str(self.imm)
            else:
                extend = ''.join(["0" for i in range(16)])
                return str(extend) + str(self.imm)
    
    #Instruction decode - identifies the opcode, splits into fields, generates control signals, register read, branch target address and jump target address calculation 
    def decode(self, code):
        self.opcode = self.machine_code[:6]
        format = self.main_decoder_unit(self.machine_code, self.opcode)
        self.format = format
        print(format)
        self.generate_control_signals(format)
        if format == 'i':
            self.imm = self.sign_extend(format, self.imm)
            #print(self.imm)
        if format != 'j':
            #print(self.rt)
            self.readData1 = register_file[self.rs]
            self.readData2 = register_file[self.rt]
            if self.regDst == 1:
                self.writeReg = self.rd
            else:
                self.writeReg = self.rt
            if self.branch == "10" or self.branch == "01":
                if self.readData1 == self.readData2 and self.jump == 0 and self.branch == "01":
                    print(self.branch)
                    self.nextpc = str(bin(int(self.nextpc, 2) + int(str(self.imm), 2) * int("100", 2)))[2:].zfill(32)
                elif self.readData1 != self.readData2 and self.jump == 0 and self.branch == "10": 
                    self.nextpc = str(bin(int(self.nextpc, 2) + int(str(self.imm), 2) * int("100", 2)))[2:].zfill(32)
        elif self.jump == 1:
            self.nextpc = "0000" + self.address + "00"
    
    #instruction execute - ALU operations
    def execute(self):
        if self.format != 'j':
            self.ALUa = self.readData1
            if self.ALUSrc == 1: #ALU Src multiplexor
                self.ALUb = self.imm
            else:
                self.ALUb = self.readData2
               # print(self.readData2)
            if self.ALUc == "0010": #add
                #print("ALUa : ", self.ALUa)
                #print("ALUb : ", self.ALUb)
                self.ALUout = bin(int(self.ALUa, 2) + int(str(self.ALUb), 2))[2:].zfill(32)
            elif self.ALUc == "0110": #sub
                if int(self.ALUa, 2) - int(str(self.ALUb), 2) >= 0:
                    self.ALUout = bin(int(self.ALUa, 2) - int(str(self.ALUb), 2))[2:].zfill(32)
                else:
                    self.ALUout = ''.join(['1' for _ in range(33 - len(bin(int(self.ALUa, 2) - int(str(self.ALUb), 2))[2:]))]) + bin(int(self.ALUa, 2) - int(str(self.ALUb), 2))[3:] 
            elif self.ALUc == "0111": #set less than
                #print("ALU a: ", self.ALUa)
                #print("ALU b: ", self.ALUb)
                if int(str(self.ALUa), 2) < int(str(self.ALUb), 2):
                    self.ALUout = bin(int("1", 10))[2:].zfill(32)
                else:
                    self.ALUout = bin(int("0", 10))[2:].zfill(32)
            elif self.ALUc == "0000":
                self.ALUout = bin(int(self.ALUa, 2) & int(str(self.ALUb), 2))[2:].zfill(32)
            elif self.ALUc == "0001":
                self.ALUout = bin(int(self.ALUa, 2) | int(str(self.ALUb), 2))[2:].zfill(32)
            elif self.ALUc == "0100":
                #print("ALU b: ", self.ALUb)
                #print("shift: ", self.shamt)
                self.ALUout = bin(int(str(self.ALUb), 2) * (pow(int("010",2), int(self.shamt, 2))))[2:].zfill(32)
            elif self.ALUc == "1000":
                self.ALUout = register_file["lo"]
            elif self.ALUc == "0101":
                self.ALUout = bin(int(self.ALUa, 2) * int(str(self.ALUb), 2))[2:].zfill(32)[32:]
                print("ALUOUT : ", self.ALUout)
                register_file["lo"] = self.ALUout

    #Memory access - Memory read and write
    def memory_access(self):
        if self.format != 'j':
            self.add = self.ALUout
            self.write = register_file[self.rt]
            if self.memWrite == 1:
                data_memory[self.add] = self.write
                print("Memory Updated", self.add, self.write)
                
            if self.memRead == 1:
                self.memReadp = data_memory[self.add]

    #Write back - write to register file
    def write_back(self):
        if self.format != 'j':
            if self.regWrite == 1:
                if self.memToreg == 1:
                    self.writeData = self.memReadp
                else:
                    self.writeData = self.ALUout
                register_file[self.writeReg] = self.writeData
                print("Register File updated", self.writeReg, self.writeData)

class Non_Pipelined_Processor:
    def __init__(self):
        self.clock = 0

    def execution_time(self, pc):
        instr = Instruction(pc)
        for i in range(len(instruction_memory)):
            instr.fetch(pc)
            if instr.machine_code == ["0"]:
                print(self.clock)
                return
            print("Machine code: " , instr.machine_code)
            self.clock += 1
            instr.decode(code)
            print("Opcode: ", instr.opcode, end = " ")
            print("rs: ", instr.rs, end = " ")
            print("rt: ", instr.rt, end = " ")
            print("rd: ", instr.rd, end = " ")
            print("imm: ", instr.imm, end = " ")
            print("funct: ", instr.funct, end = " ")
            print("readData1: ", instr.readData1, end = " ")
            print("readData2: ", instr.readData2, end = " ")
            print("regDst: ", instr.regDst, end = " ")
            print("regWrite: ", instr.regWrite, end = " ")
            print("ALUOp: ", instr.ALUOp, end = " ")
            print("ALUc: ", instr.ALUc, end = " ")
            print("ALUSrc: ", instr.ALUSrc, end = " ")
            print("branch: ", instr.branch, end = " ")
            self.clock += 1
            instr.execute()
            print("ALUa: ", instr.ALUa, end = " ")
            print("ALUb: ", instr.ALUb, end = " ")
            print("ALUout: ", instr.ALUout, end = " ")
            self.clock += 1
            instr.memory_access()
            self.clock += 1
            instr.write_back()
            self.clock += 1
            print("PC, clock: ", instr.pc, self.clock)
            if instruction_memory[instr.nextpc] != ' ' or instruction_memory[instr.nextpc] != '':
                instr = Instruction(instr.nextpc)
            else:
                print("Clock: ", self.clock)
                return
        

print(instruction_memory)
print(register_file)
print(data_memory)
proc1 = Non_Pipelined_Processor()
if code == 'C':
    proc1.execution_time(bin(int("0040008c", 16))[2:].zfill(32))
else:
    proc1.execution_time(bin(int("0040004c", 16))[2:].zfill(32))
#for i in list(data_memory.keys()):
#   print(i, ":", data_memory[i])
