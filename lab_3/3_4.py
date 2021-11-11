def sift_down(arr, i, size):
    s1 = i * 2 + 1
    s2 = i * 2 + 2
    if (s1 < size and arr[s1][0] < arr[i][0]):
        minimum = s1
    else:
        minimum = i
    if (s2 < size and arr[s2][0] < arr[minimum][0]):
        minimum = s2
    if (minimum != i):
        arr[minimum], arr[i] = arr[i], arr[minimum]
        sift_down(arr, minimum, size)


def sift_up(arr, i):
    parent = (i - 1) // 2
    if i != 0 and arr[i][0] < arr[parent][0]:
        arr[i], arr[parent] = arr[parent], arr[i]
        sift_up(arr, parent)


file = open("priorityqueue.in", 'r')
f_out = open('priorityqueue.out', 'w')


arr = [[0 for i in range(2)] for j in range(70000)]
t = 0
place = 0
s = file.readline().split()


while(s):
    t += 1
    if s[0] == "push":
        arr[place][0] = int(s[1])
        arr[place][1] = t
        sift_up(arr, place)
        place += 1
    elif s[0] == "extract-min":
        if place == 0:
            print('*', file=f_out)
        else:
            print(arr[0][0], file=f_out)
            leng = place - 1
            arr[0], arr[leng] = arr[leng], arr[0]
            place -= 1
            sift_down(arr, 0, leng)
    elif s[0] == "decrease-key":
        h = int(s[1])
        for i in range(place):
            if arr[i][1] == h:
                break
        arr[i][0] = int(s[2])
        sift_up(arr, i)
    s = file.readline().split()