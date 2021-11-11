import random

def QS(massive):
    if len(massive) <= 1:
        return massive
    else:
        q = random.choice(massive)
        L = []
        M = []
        R = []
        for elem in massive:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QS(L) + M + QS(R)

file = open("smallsort.in.", "r")
lines = file.readlines()

lines.pop(0)
line = [int(i) for i in lines[0].split()]

line = QS(line)

res = ' '.join(map(str, line))

file_output = open("smallsort.out", 'w')
file_output.write(res)
file_output.close()
