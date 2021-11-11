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

file = open("sortland.in.", "r")
lines = file.readlines()

lines.pop(0)
line = [float(i) for i in lines[0].split()]
m = line.copy()

line = QS(line)

res = str(m.index(line[0]) + 1) + ' ' + str(m.index(line[len(line) // 2]) + 1) + ' ' + str(m.index(line[len(line) - 1]) + 1)

file_output = open("sortland.out", 'w')
file_output.write(res)
file_output.close()
