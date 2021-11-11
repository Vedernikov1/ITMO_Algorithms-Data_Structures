def radix_sort(arr):
    for i in range(int(n[2])):
        C = [0] * 26
        for j in range(len(arr)):
            d = ord(arr[j][len(arr[0]) - 1 - i]) - 97
            C[d] += 1
        for j in range(1, 26):
            C[j] += C[j - 1]
        B = [0] * len(arr)
        for j in range(len(arr) - 1, -1, -1):
            d = ord(arr[j][len(arr[0]) - i - 1]) - 97
            counter = C[d] - 1
            B[counter] = arr[j]
            C[d] -= 1
        arr = B.copy()
    return arr


file = open("radixsort.in")
n = file.readline().split()
arr = []
for i in range(int(n[0])):
    t = file.readline().strip()
    arr.append(t)

arr = radix_sort(arr)

f_out = open('radixsort.out', 'w')
for i in range(len(arr)):
    # if i != len(arr) - 1:
    f_out.write(str(arr[i] + '\n').strip() + '\n')
    # else:
    #     f_out.write(arr[i])
file.close()
f_out.close()