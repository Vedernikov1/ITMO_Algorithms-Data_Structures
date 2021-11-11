input_file = open('queue.in', 'r')
output_file = open('queue.out', 'w')


def queue_plus(queue, elem):
    queue = elem + queue
    return queue


def queue_minus(queue):
    print(queue[len(queue) - 1], file=output_file)
    queue.pop(len(queue) - 1)
    return queue


queue = []
number_of_comands = input_file.readline()
list_of_comands = input_file.readlines()

for comand in list_of_comands:
    comand = comand.split()
    if comand[0] == '+':
       queue = queue_plus(queue, [comand[1]])
    else:
        queue_minus(queue)

