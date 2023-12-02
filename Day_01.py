# Day 01
file = open(r'C:\Users\Trevor\Desktop\Python Projects\AoC_2023\day01_data.txt')
data = file.read().split('\n')
for x in range(len(data)):
    data[x] = list(data[x])

lx = len(data)
array = [[0 for x in range(50)] for x in range(lx)]
indarray = [[0 for x in range(50)] for x in range(lx)]

cnt = 0
for x in range(lx):
    ly = len(data[x])
    for y in range(ly):
        if data[x][y] in {"0","1","2","3","4","5","6","7","8","9"}:
            array[x][cnt] = int(data[x][y])
            indarray[x][cnt] = 1
            cnt += 1
    cnt = 0

farray = 0
for x in range(lx):
    ly = len(data[x])
    tot = sum(indarray[x]) - 1
    farray += array[x][0] * 10 + array[x][tot]

print(farray)         

# Part 2