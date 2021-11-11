file = open("aplusb.in.", "r")
lines = file.readlines()

file_output = open("aplusb.out", 'w')
file_output.write(str(sum([int(i) for i in lines[0].split()])))
file_output.close()
