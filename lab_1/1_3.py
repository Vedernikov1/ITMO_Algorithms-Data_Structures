file = open("turtle.in.", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = [int(k) for k in lines[i].split()]


size = lines[0]
width = int(size[1])
height = int(size[0])
lines.pop(0)


i = height - 2
while(i+1):
    lines[i][0] += lines[i+1][0]
    i -= 1
lines[height-1] = [sum(lines[height-1][0:j+1]) for j in range(width)]

for i in range(1, min(width, height)):
    k = height - i - 1
    while(k+1):
        lines[k][i] += max(lines[k+1][i], lines[k][i-1])
        k -= 1
    for k in range(i + 1, width):
        lines[height-1-i][k] += max(lines[height-1-i][k-1], lines[height-i][k])


res = lines[0][width-1]

file_output = open("turtle.out", 'w')
file_output.write(str(res))
file_output.close()
