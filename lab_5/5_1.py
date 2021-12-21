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


def search(head, count):
    global res
    res = max(res, count)
    if head.left: search(head.left, count + 1)
    if head.right: search(head.right, count + 1)


f_input = open('height.in', 'r')
f_output = open('height.out', 'w')
lines = f_input.readlines()
if lines: lines.pop(0)
arr = [list(map(int, elem.strip().split())) for elem in lines]
res = 0

if len(arr):
    head = TreeNode(arr[0])
    make(head, arr)
    search(head, 1)

print(res, file=f_output)