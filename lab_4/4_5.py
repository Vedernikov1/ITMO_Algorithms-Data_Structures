def bin_search(test, key):
    left = 0
    right = len(test)
    while left < right:
        middle = (left + right) // 2
        if test[middle] >= key:
            right = middle
        else:
            left = middle + 1
    return left


file_input = open("binsearch.in", 'r')
file_output = open("binsearch.out", 'w')

_ = int(file_input.readline())
list_of_nums = [int(i) for i in file_input.readline().split()]
num_of_keys = file_input.readline()
keys = [int(i) for i in file_input.readline().split()]

for key in keys:
    left_index = bin_search(list_of_nums, key)
    right_index = bin_search(list_of_nums, key + 1)

    if left_index >= len(list_of_nums):
        print('-1', '-1', file=file_output)
    elif list_of_nums[left_index] != key:
        print('-1', '-1', file=file_output)
    else:
        print(left_index + 1, right_index, file=file_output)
