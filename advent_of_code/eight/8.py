import copy
import sys
with open('input') as f:
    lines = [line.strip('\n').split(' ') for line in f]

print(lines)
# Part one
# Variable for storing acc value and keep track of orders executed.


accumulator = 0
executed = set()
index = 0
while True:
    order = lines[index][0]
    value = int(lines[index][1])
    if index in executed:
        break
    executed.add(index)
    if order == 'acc':
        accumulator += value
        index += 1
    elif order == 'nop':
        index += 1
    elif order == 'jmp':
        index += value
print(f"Part one answer - accumulator value: {accumulator}")
