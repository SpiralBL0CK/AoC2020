with open('input.txt') as f:
    data = [line.strip() for line in f]
    
def bs(cmds,letter,end,start=0):
    for char in cmds:
        mid = (end - start ) // 2 
        if char == letter:
            end = mid + start
        else:
            start = start + mid +1
    return end

def seatid(line):
    row = bs(line[:-3],'F',127)
    col = bs(line[-3:],'L',7)
    idd = row * 8 + col
    return idd




maxid = max(seatid(l) for l in data)
print(maxid)