# Opcodes for r_format instructions. (All zero)
r_format = {'sll': 0x00, 
            'srl' : 0x00, 
            'sra' : 0x00, 
            'mult' : 0x00, 
            'multu': 0x00, 
            'div': 0x00, 
            'divu': 0x00, 
            'sllv': 0x00, 
            'srlv': 0x00, 
            'srav': 0x00, 
            'add': 0x00, 
            'addu': 0x00, 
            'sub': 0x00, 
            'subu': 0x00, 
            'and': 0x00, 
            'or': 0x00, 
            'xor': 0x00, 
            'nor': 0x00, 
            'slt': 0x00, 
            'sltu': 0x00,
            'mflo': 0x00
            }

# Opcodes for i_format instructions.
i_format = {'beq': 0x04, 
            'bne': 0x05, 
            'blez': 0x06, 
            'bgtz': 0x07, 
            'addi': 0x08, 
            'addiu': 0x09, 
            'slti': 0x0A, 
            'sltiu': 0x0B, 
            'andi': 0x0C, 
            'ori': 0x0D, 
            'xori': 0x0E, 
            'lui': 0x0F, 
            'lb': 0x20, 
            'lh': 0x21, 
            'lw': 0x23, 
            'lbu': 0x24, 
            'lhu': 0x25, 
            'sb': 0x28, 
            'sh': 0x29, 
            'sw': 0x2B
            }

# Opcodes for j_format instructions.
j_format = {'j': 0x02, 
            'jal': 0x03, 
            'jr': 0x00
            }

# Values for all the registers.
registers = {'$0': 0, 
             '$at': 1, 
             '$v0': 2, 
             '$v1': 3, 
             '$a0': 4, 
             '$a1': 5, 
             '$a2': 6, 
             '$a3': 7, 
             '$t0': 8, 
             '$t1': 9, 
             '$t2': 10, 
             '$t3': 11, 
             '$t4': 12, 
             '$t5': 13, 
             '$t6': 14, 
             '$t7': 15, 
             '$s0': 16, 
             '$s1': 17, 
             '$s2': 18, 
             '$s3': 19, 
             '$s4': 20, 
             '$s5': 21, 
             '$s6': 22, 
             '$s7': 23, 
             '$t8': 24, 
             '$t9': 25, 
             '$k0': 26, 
             '$k1': 27, 
             '$gp': 28, 
             '$sp': 29, 
             '$fp': 30, 
             '$ra': 31 
            }


# Memory = []

# This function converts an integer to binary with N total digits, using necessary padding with 0's.
def binaryN(num, N):
    if num < 0:
        num = int(0xffffffff) + num
    return (f"{num:0{N}b}")

# This function converts a 32 bit binary number given as a string to an 8 Bit hexadecimal string.
def bin4hex(string):
    hexDict = {'0000': '0',
               '0001': '1',
               '0010': '2',
               '0011': '3',
               '0100': '4',
               '0101': '5',
               '0110': '6',
               '0111': '7',
               '1000': '8',
               '1001': '9',
               '1010': 'a',
               '1011': 'b',
               '1100': 'c',
               '1101': 'd',
               '1110': 'e',
               '1111': 'f'
                }
    return ('0x' + hexDict[string[0:4]] + hexDict[string[4:8]] + hexDict[string[8:12]] + hexDict[string[12:16]] + hexDict[string[16:20]] + hexDict[string[20:24]] + hexDict[string[24:28]] + hexDict[string[28:32]])

# This function holds addresses of statements as given by MARS (Hardcoded)
def jumpAddress(something):

    jumpDict = {
        'done' : 35,
        'kloop': 9,
        'jloop' : 3,
        'iloop' : 1048585,

    }
    return jumpDict[something]

# This function gives shift amounts.
def shamt(something):
    shifts = ['sll', 'srl', 'sra']
    if (something in shifts):
        return 10
    else:
        return 0

# This function gives the 'func' value in the machine code.
def func(something):
    funcDict = {
            'sll': 0, 
            'srl' : 2, 
            'sra' : 3, 
            'mult' : 24, 
            'multu': 25, 
            'div': 26, 
            'divu': 27, 
            'sllv': 4, 
            'srlv': 6, 
            'srav': 7, 
            'add': 32, 
            'addu': 33, 
            'sub': 34, 
            'subu': 35, 
            'and': 36, 
            'or': 37, 
            'xor': 38, 
            'nor': 39, 
            'slt': 42, 
            'sltu': 43
            }
    return funcDict[something]


# This function returns the 32 bit machine code for the instruction it is passed.
def MachineCodeMaker(l):
    i = 0
    # Each conditional statement is made to filter different types of functions and make the necessary binary string.
    if processed[i] == 'sll': 
        return ('00000000000' + binaryN(registers[l[i+2]],5) + binaryN(registers[l[i+1]],5) + binaryN(int(l[i+3]),5) + '000000')
    elif processed[i] in ['lw', 'sw']:
        return (binaryN(int(i_format[l[i]]),6) + binaryN(registers[l[i+3]],5) + binaryN(registers[l[i+1]],5) + binaryN(int(l[i+2]),16))
    elif processed[i] in ['beq', 'bne']:
        return (binaryN(int(i_format[l[i]]),6) + binaryN(registers[l[i+1]],5) + binaryN(registers[l[i+2]],5) + binaryN(jumpAddress(l[i+3]),16))
    elif processed[i] in ['mult', 'multu']:
        return ('000000' + binaryN(registers[l[i+1]],5) + binaryN(registers[l[i+2]],5) + '0000000000' + binaryN(func(l[i]),6))
    elif processed[i] == 'mflo':
        return ('0000000000000000' + binaryN(registers[l[i+1]],5) + '00000010010')
    elif processed[i] in r_format.keys():
        return (binaryN(int(r_format[l[i]]),6) + binaryN(registers[l[i+2]],5) + binaryN(registers[l[i+3]],5) + binaryN(registers[l[i+1]],5) + binaryN(shamt(l[i]),5) + binaryN(func(l[i]),6))
    elif processed[i] in i_format.keys():
        return (binaryN(int(i_format[l[i]]),6) + binaryN(registers[l[i+2]],5) + binaryN(registers[l[i+1]],5) + binaryN(int(l[i+3]),16))
    elif processed[i] in j_format.keys():
        if (processed[i] == 'j' and processed[i+1] == 'jloop'):
            return ('00001000000100000000000000010000')
        return (binaryN(int(j_format[l[i]]),6) + binaryN(jumpAddress(l[i+1]),26))


# Open the file with the code written for matrix multiplication.
f = open('matrixcore.asm', 'r')

# Go through each line.
for line in f.readlines():
    current = line[:-1]
    commentless = (current.split('#')) # Seperate the comments
    processed = (commentless[0].replace(',', ' ').replace('(', ' ').replace(')', ' ').split()) # Split the line so we isolate the values
    
    if len(processed) < 2: # Blank lines and statements ommitted.
        continue
    if ((processed[0] in r_format.keys()) or (processed[0] in j_format.keys()) or (processed[0] in i_format.keys())):
        code = bin4hex(MachineCodeMaker(processed))
        txt = open("machinematrix.txt", "a")
        # for e in processed:
        #     txt.write(e + " ")
        # txt.write("\n")
        txt.write(code + "\n")
        txt.close()

f.close() # Close the matrix multiplication file

#IMT2022571
#IMT2022100