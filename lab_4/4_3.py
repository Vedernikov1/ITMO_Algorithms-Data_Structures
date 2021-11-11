input_file = open('brackets.in', 'r')
output_file = open('brackets.out', 'w')


class Stack:
    def __init__(self):
        self.flag = 1
        self.stack = []

    def plus(self, brackets):
        self.stack.append(brackets)

    def minus(self):
        self.stack.pop(len(self.stack) - 1)


list_of_lines = input_file.readlines()

for line in list_of_lines:

    line = line.strip()

    stack = Stack()

    for symbol in line:
        if symbol == '(' or symbol == '[':
            stack.plus(symbol)
        elif symbol == ')':
            if len(stack.stack):
                if stack.stack[len(stack.stack) - 1] == '(':
                    stack.minus()
                else:
                    stack.flag = 0
                    print('NO', file=output_file)
                    break
            else:
                stack.flag = 0
                print('NO', file=output_file)
                break

        elif symbol == ']':
            if len(stack.stack):
                if stack.stack[len(stack.stack) - 1] == '[':
                    stack.minus()
                else:
                    stack.flag = 0
                    print('NO', file=output_file)
                    break
            else:
                stack.flag = 0
                print('NO', file=output_file)
                break

    if stack.flag and line:
        if len(stack.stack) == 0:
            print('YES', file=output_file)
        else:
            print('NO', file=output_file)


