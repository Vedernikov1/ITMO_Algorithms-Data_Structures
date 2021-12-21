def hf(key):
    res, p = 0, 239
    for i in key:
        res += ord(i) * p
        p *= 239
    return res


def put(key, val):
    global num
    pos = hf(key) % num
    for i in range(len(arr[pos])):
        if arr[pos][i][0] == key:
            arr[pos][i][1] = val
            return
    arr[pos].append([key, val])


def delete(key):
    global num
    pos = hf(key) % num
    length, i = len(arr[pos]), 0
    while i < length:
        # print(i)
        # print(i, len(arr[pos]), arr[pos][i])
        if arr[pos][i][0] == key:
            arr[pos].pop(i)
            length -= 1
        i += 1


def get(key):
    global num
    res = 'none'
    pos = hf(key) % num
    for i in range(len(arr[pos])):
        if arr[pos][i][0] == key:
            res = arr[pos][i][1]
    return res


num = int(1e5)
arr = [[] for _ in range(num)]

f_in = open('map.in', 'r')
f_out = open('map.out', 'w')

list_of_commands = f_in.readlines()

for s in list_of_commands:
    # print(arr)
    command = s.split()
    if command[0] == 'put':
        put(command[1], command[2])
    elif command[0] == 'delete':
        delete(command[1])
    else:
        print(get(command[1]), file=f_out)