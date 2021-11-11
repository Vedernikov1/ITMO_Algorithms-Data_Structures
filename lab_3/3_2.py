def HS(arr):
    MX(arr)
    i = len(arr) - 1
    while(i):
        arr[0], arr[i] = arr[i], arr[0]
        MH(arr, 0, i)
        i -= 1


def MX(arr):
    start = (len(arr) - 2) // 2
    while start >= 0:
        MH(arr, start, len(arr))
        start -= 1


def MH(arr, i, size):
    s1 = i * 2 + 1
    s2 = i * 2 + 2
    if (s1 < size and arr[s1] > arr[i]):
        largest = s1
    else:
        largest = i
    if (s2 < size and arr[s2] > arr[largest]):
        largest = s2
    if (largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]
        MH(arr, largest, size)


file = open("sort.in")
n = int(file.readline())
arr = list(map(int, file.readline().split()))

HS(arr)
arr = ' '.join(map(str, arr))
print(arr)
f_out = open('sort.out', 'w')

f_out.write(str(arr))