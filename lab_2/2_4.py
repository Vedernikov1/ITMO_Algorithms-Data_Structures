file = open("antiqs.in.", "r")
n = int(file.readline())
m = [i for i in range(1, n + 1)]
for i in range(n):
    m[i//2], m[i] = m[i], m[i//2]

res = ' '.join(map(str, m))

file_output = open("antiqs.out", 'w')
file_output.write(res)

file_output.close()
file.close()

