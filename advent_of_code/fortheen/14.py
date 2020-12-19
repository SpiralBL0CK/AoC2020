from itertools import product
from parse import parse

def as_int36(b):
    return f'{int(bin(int(b))[2:]):036}'

def apply_mask(bits,mask):
    s = ""
    for b,m in zip(bits,mask):
        if m == 'X':
            s += b
        else:
            s +=  m
    return s

def a(lines):
    mem = {}
    mask = None
    for l in lines:
        op,value = parse('{} = {}',l)
        if 'mask' in op:
            mask = value
        else:
            number = as_int36(value)
            address = parse('mem[{:d}]',op)[0]
            #print(int(apply_mask(number,mask),2))    
            mem[address] = int(apply_mask(number,mask),2)
    return sum(mem.values())


def check_polimorphysm(bits,mask):
    adr_bits = []
    res = []
    for b,m in zip(bits,mask):
        if m == '0':
            adr_bits.append(b)
        elif m == '1':
            adr_bits.append('1')
        else:
            adr_bits.append('01')
    for a in map("".join,product(*adr_bits)):
        res.append(int(a,2))
    return res

def b(lines):
    mem = {}
    mask = None
    for l in lines:
        op,value = parse('{} = {}',l)
        if 'mask' in op:
            mask = value
        else:
            number = int(value)
            address = parse('mem[{:d}]',op)[0]
            addresses = check_polimorphysm(as_int36(address),mask)
            for addr in addresses:
                mem[addr] = number
    return sum(mem.values())

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
    
    print(a(lines))
    print(b(lines))