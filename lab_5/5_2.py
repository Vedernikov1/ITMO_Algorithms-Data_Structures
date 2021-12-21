import sys

sys.setrecursionlimit(1000000)


class TreeNode:
    def __init__(self, info):
        self.info = info
        self.value = info[0]
        self.left = None
        self.right = None


def make(head, arr):
    # print(head.value)
    if head.info[1]:
        left = TreeNode(arr[head.info[1] - 1])
        head.left = left
        make(left, arr)
    if head.info[2]:
        right = TreeNode(arr[head.info[2] - 1])
        head.right = right
        make(right, arr)


def search(value_min, head, value_max):
    global res
    if head.value <= value_min or head.value >= value_max:
        res = False
    if head.left and res: search(value_min, head.left, head.value)
    if head.right and res: search(head.value, head.right, value_max)


f_input = open('check.in', 'r')
f_output = open('check.out', 'w')

lines = f_input.readlines()
lines.pop(0)
arr = [list(map(int, elem.strip().split())) for elem in lines]
res = True

if len(arr):
    head = TreeNode(arr[0])
    make(head, arr)
    search(-float('inf'), head, float('inf'))

if res:
    print('YES', file=f_output)
else:
    print('NO', file=f_output)