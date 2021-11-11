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


file = open("race.in.", "r")
results = []

n = int(file.readline())
for i in range(n):
    elem = file.readline().split()
    results.append([elem[0], i, elem[1]])

results = QS(results)
t = ''
file_output = open("race.out", 'w')

for elem in results:
    if elem[0] != t:
        file_output.write('=== '+elem[0]+' ===\n')
    file_output.write(elem[2] + '\n')
    t = elem[0]

file_output.close()
file.close()