file = open("isheap.in.", "r")
n = int(file.readline())
arr = [int(i) for i in file.readline().split()]

f = 1

for i in range(1, n//2 + 2):
    if 2*i < n:
        if arr[i-1] > arr[2*i - 1]:
            f = 0
            break
    if 2*i + 1 < n:
        if arr[i-1] > arr[2*i - 1]:
            f = 0
            break

file_output = open("isheap.out", 'w')

if f:
    file_output.write('YES')
else:
    file_output.write('NO')

file_output.close()
