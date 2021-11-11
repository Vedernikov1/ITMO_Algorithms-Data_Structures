import random


def QS(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        Left = []
        Middle = []
        Right = []
        for elem in arr:
            if elem < q:
                Left.append(elem)
            elif elem > q:
                Right.append(elem)
            else:
                Middle.append(elem)
        return QS(Left) + Middle + QS(Right)


file = open("sort.in.", "r")
lines = file.readlines()

lines.pop(0)
line = [int(i) for i in lines[0].split()]

line = QS(line)

res = ' '.join(map(str, line))

file_output = open("sort.out", 'w')
file_output.write(res)
file_output.close()