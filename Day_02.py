# Day 02
file = open(r'C:\Users\Trevor\Desktop\Python Projects\AoC_2023\day02_data.txt')
data = file.read().split('\n')
for x in range(len(data)):
    a = data[x].split(":", 1)
    data[x] = a[1].split(";")

l = len(data)
possible = [1 for x in range(l)]
answ = 0
sumx = 0

for x in range(l):
    r = 0
    b = 0
    g = 0
    for y in range(len(data[x])):
        grab = data[x][y].split(",")
        for z in range(len(grab)):
            intcol = grab[z].split(" ")
            if "red" in intcol[2]:
                if int(intcol[1]) > r:
                    r = int(intcol[1])
            if "green" in intcol[2]:
                if int(intcol[1]) > g:
                    g = int(intcol[1])                     
            if "blue" in intcol[2]:
                if int(intcol[1]) > b:
                    b = int(intcol[1])
            if r > 12 or g > 13 or b > 14:
                possible[x] = 0  
    if possible[x] == 1:
        answ += x + 1
    sumx += r*g*b

print(sumx)  
print(answ)