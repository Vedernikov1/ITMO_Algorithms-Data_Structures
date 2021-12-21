import sys

sys.setrecursionlimit(1000000)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(root, new):
    if root is None: return TreeNode(new)
    elif new < root.value: root.left = insert(root.left, new)
    elif new > root.value: root.right = insert(root.right, new)
    return root


def delete(root, value):
    if root is None: return root
    if value < root.value: root.left = delete(root.left, value)
    elif value > root.value: root.right = delete(root.right, value)
    elif root.left is None and root.right is None: root = None
    elif root.right is not None: root = root.right
    elif root.left is not None: root = root.left
    elif root.left is not None and root.right is not None:
        root.value = find_min(root.right).value
        root.right = delete(root.right, root.value)
    return root


def next(tree, val):
    next = None
    while tree is not None:
        if tree.value > val:
            next = tree
            tree = tree.left
        else: tree = tree.right
    return next.value


def prev(tree, val):
    prev_item = None
    while tree is not None:
        if tree.value >= val: tree = tree.left
        elif tree.value < val:
            prev_item = tree
            tree = tree.right
    if prev_item is None: return 999999999999999
    else: return prev_item.value


def find_min(root):
    if root.left: return find_min(root.left)
    return root


def exists(root, value):
    if not root: return 'false'
    elif root.value == value: return 'true'
    elif value < root.value: return exists(root.left, value)
    elif value > root.value: return exists(root.right, value)


head = TreeNode(999999999999999)
f_input = open('bstsimple.in', 'r')
f_output = open('bstsimple.out', 'w')

list_of_requests = f_input.readlines()
if list_of_requests:
    for request in list_of_requests:
        request_modified = request.split()
        if request_modified[0] == 'insert':
            new_node = int(request_modified[1])
            insert(head, new_node)
        elif request_modified[0] == 'delete': head = delete(head, int(request_modified[1]))
        elif request_modified[0] == 'prev':
            res = prev(head, int(request_modified[1]))
            if res == 999999999999999:
                print('none', file=f_output)
            else:
                print(res, file=f_output)
        elif request_modified[0] == 'exists':print(exists(head, int(request_modified[1])), file=f_output)
        else:
            res = next(head, int(request_modified[1]))
            if res == 999999999999999:
                print('none', file=f_output)
            else:
                print(res, file=f_output)

