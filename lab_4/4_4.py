file_input = open('postfix.in', 'r')
file_output = open('postfix.out', 'w')


class Stack:
    def __init__(self):
        self.stack = []

    def stack_erase(self):
        position = len(self.stack) - 1
        elem = self.stack[position]
        self.stack.pop(position)
        return elem

    def stack_push(self, elem):
        self.stack.append(elem)


stack = Stack()
post_line = file_input.readline().split()

for symbol in post_line:
    if symbol == '+':
        # Совершаем операцию с двумя последними элементами в стеке
        stack.stack_push(stack.stack_erase() + stack.stack_erase())
    elif symbol == '*':
        stack.stack_push(stack.stack_erase() * stack.stack_erase())
    elif symbol == '-':
        elem_1 = stack.stack_erase()
        elem_2 = stack.stack_erase()
        stack.stack_push(elem_2 - elem_1)
    else:
        stack.stack_push(int(symbol))

print(stack.stack_erase(), file=file_output)


