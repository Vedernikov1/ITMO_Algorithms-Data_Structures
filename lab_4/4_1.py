input_file = open('stack.in', 'r')
output_file = open('stack.out', 'w')


def stack_plus(stack, elem):
    stack.append(elem)
    return stack


def stack_minus(stack):
    print(stack[len(stack) - 1], file=output_file)
    stack.pop(len(stack) - 1)
    return stack


stack = []
number_of_comands = input_file.readline()
list_of_comands = input_file.readlines()

for comand in list_of_comands:
    comand = comand.split()
    if comand[0] == '+':
        stack_plus(stack, comand[1])
    else:
        stack_minus(stack)

