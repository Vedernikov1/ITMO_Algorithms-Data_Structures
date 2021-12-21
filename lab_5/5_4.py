input_file = open("quack.in", "r")
output_file = open("quack.out", "w")

list_of_commands = input_file.read().split()
arr, registers = [], []

shift, num_of_letters = 97, 26

for i in range(num_of_letters):
    registers.append((chr(i + shift),0))
registers = dict(registers)

labels = {}
for i in range(len(list_of_commands)):
    if list_of_commands[i][0] == ':':
        labels[list_of_commands[i][1:]] = i

i = 0
while i < len(list_of_commands):
    line = list_of_commands[i]
    if line == "Q": break
    if line in "+-*/%":
        arg1 = arr.pop(0)
        arg2 = arr.pop(0)
        if line in "/%" and arg2 == 0: arr.append(0)
        else: arr.append(int(eval(str(arg1) + line + str(arg2))) & 65535)

    elif line[0] == "P":
        out = registers[line[1]] if len(line) > 1 else arr.pop(0)
        print(out, file=output_file)
    elif line[0] == "C":
        out = chr(registers[line[1]] if len(line) > 1 else arr.pop(0) & 255)
        print(out, file=output_file, end="")

    elif line[0] == "J": i = labels[line[1:]]
    elif line[0] == "Z": i = labels[line[2:]] if registers[line[1]] == 0 else i
    elif line[0] == "E": i = labels[line[3:]] if registers[line[1]] == registers[line[2]] else i
    elif line[0] == "G": i = labels[line[3:]] if registers[line[1]] > registers[line[2]] else i

    elif line[0] == ">": registers[line[1]] = arr.pop(0)
    elif line[0] == "<": arr.append(registers[line[1]])
    elif line[0] != ":": arr.append(int(line))
    i += 1
