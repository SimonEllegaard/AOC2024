import os

input = open(os.getcwd() + "\\day1.txt").read().strip()
lines = []
for line in input.split('\n'):
    line = line.strip()
    lines.append((line))

col1 = []
col2 = []
for line in lines:
    items = line.split(' ')
    col1.append(items[0])
    col2.append(items[3])
col1.sort()
col2.sort()
res = 0
item_index = 0
for item in col1:
    res += abs(int(item) - int(col2[item_index]))
    item_index += 1
#part 1
print(res)

res = 0
for item in col1:
    count = col2.count(item)
    res += count * int(item)
print(res)