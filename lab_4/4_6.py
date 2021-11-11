input_file = open('garland.in', 'r')
output_file = open('garland.out', 'w')

k = input_file.readline().split()
n = int(k[0])
A = float(k[1])

arr = []
for i in range(n+1):
    arr.append(0)

arr[0] = A
left = 0
right = A
last = 0

while right - left > 0.000001:
    f = 1
    arr[1] = (left + right) / 2
    for i in range(2, n):
        arr[i] = 2 * (arr[i - 1]) - arr[i - 2] + 2
        if arr[i] < 0:
            f = 0
            break
    if f:
        right = arr[1]
        last = arr[n-1]
    else:
        left = arr[1]

print(round(last, 2), file=output_file)
