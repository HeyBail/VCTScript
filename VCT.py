import sys

# read arguments
programFilepath = sys.argv[1]

######################
# tokenize program
######################

# read file lines
programLines = []
with open(programFilepath, "r") as programFile:
    programLines = [line.strip() for line in programFile.readlines()]

program = []
tokenCounter = 0
labelTracker = {}
for line in programLines:
    parts = line.split()
    opcode = parts[0]

    # check for empty line
    if opcode == "":
        continue

    # check if it's a label
    if opcode.endswith(":"):
        labelTracker[opcode[:-1]] = tokenCounter
        continue

    # store opcode token
    program.append(opcode)
    tokenCounter += 1

    # handle each opcode
    if opcode == "STACK":
        # expecting a number
        string = int(parts[1])
        program.append(string)
        tokenCounter += 1
    if opcode == "HOLD":
        # expecting a string literal
        string = parts[1]
        program.append(string)
        tokenCounter += 1
    elif opcode == "/a":
        #parse string literal
        stringLiteral = ' '.join(parts[1:])[1:-1]
        program.append(stringLiteral)
        tokenCounter += 1
    elif opcode == "TP":
        # read label
        label = parts[1]
        program.append(label)
        tokenCounter += 1
    elif opcode == "LURK":
        # read label
        label = parts[1]
        program.append(label)
        tokenCounter += 1

######################
# interpret program
######################

class Stack:
    def __init__(self,size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]
    
    def pushBottom(self, number):
        for i in range(self.sp, -1, -1):
            self.buf[i+1] = self.buf[i]
        self.buf[0] = number
        self.sp += 1

    def popBottom(self):
        number = self.buf[0]
        for i in range(0, self.sp):
            self.buf[i] = self.buf[i+1]
        self.sp -= 1
        return number

pc = 0
stack = Stack(256)

while pc >= 0 and pc < len(program):
    opcode = program[pc]
    pc += 1
    if opcode == "HOLD": # PUSH string
        value = program[pc]
        pc += 1
        stack.push(value)
    elif opcode == "STACK": # PUSH number
        value = program[pc]
        pc += 1
        stack.push(value)
    elif opcode == "PEEK": # POP
        value = chr(stack.pop())
        print (value)
    elif opcode == "CONTACT": # ADD
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "RETAKE": # SUB
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "CLUTCH": # MUL
        a = stack.pop()
        b = stack.pop()
        stack.push(a*b)
    elif opcode == "FLANK": # DIV
        a = stack.pop()
        b = stack.pop()
        stack.push(b/a)
    elif opcode == "/a": # PRINT
        stringLiteral = program[pc]
        pc += 1
        print (stringLiteral)
    elif opcode == "THROW": # POP and PRINT
        value = stack.pop()
        print (value)
    elif opcode == "ENTRY": # READ int
        string = int(input(""))
        stack.push(string)
    elif opcode == "PING": # READ string
        string = (input(""))
        stack.push(string)
    elif opcode == "TP": # JUMP.EQ.0
        string = stack.top()
        if string == 0:
            pc = labelTracker[program[pc]] 
        else:
            pc += 1
    elif opcode == "LURK": # JUMP.GR.0
        string = stack.top()
        if string > 0:
            pc = labelTracker[program[pc]] 
        else:
            pc += 1
    elif opcode == "CLONING": # duplicate top
        stack.push(stack.top())
    elif opcode == "ROTATE": # pop bottom, push to top
        stack.push(stack.popBottom())
    elif opcode == "TRADE": # pop top, push to bottom
        stack.pushBottom(stack.pop())
    elif opcode == "HIT": # decrement top
        stack.push(stack.pop() - 1)
    elif opcode == "STALL": # PUSH 0
        stack.push(0)
    elif opcode == "PICK": # incement top
        stack.push(stack.pop() + 1)
    elif opcode == "SPLIT": # SLICE
        string = stack.pop()
        for char in reversed(string):
            stack.push(ord(char))
    elif opcode == "SAVE" or opcode == "FF": # HALT
        break
print('')