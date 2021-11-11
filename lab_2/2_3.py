res = 0


file = open("inversions.in")
n = int(file.readline())
arr = list(map(int, file.readline().split()))


def merge_sort(m):
    if len(m) <= 1:
        return m
    return merge(merge_sort(m[:len(m) // 2]), merge_sort(m[len(m) // 2:]))


def merge(L, R):
    global res
    l_i = 0
    r_i = 0
    m = []
    for _ in range(len(L) + len(R)):
        if l_i < len(L) and r_i < len(R):
            if L[l_i] <= R[r_i]:
                m.append(L[l_i])
                l_i += 1
            else:
                m.append(R[r_i])
                r_i += 1
                res += len(L) - l_i
        elif l_i == len(L):
            m.append(R[r_i])
            r_i += 1
        elif r_i == len(R):
            m.append(L[l_i])
            l_i += 1
    return m



f_out = open('inversions.out', 'w')

merge_sort(arr)

f_out.write(str(res))
