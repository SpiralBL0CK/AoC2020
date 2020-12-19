import re

if __name__ == '__main__':
    cnt = 0
    # read in the input file as a list of key value pairs aka python dictionary
    data = [{
        (key := l.split(":"))[0]: key[1]
        for l in line.replace("\n", " ").strip().split(" ")
    }
    for line in open('input').read().strip().split('\n\n')]
    
    for line in data:
        if 'byr' in line and \
                'iyr' in line and \
                'eyr' in line and \
                'hgt' in line and \
                'hcl' in line and \
                'ecl' in line and \
                'pid' in line:
                cnt +=0
        else:
            continue

        if not 1920 <= int(line['byr']) <= 2002:
            continue
        if not 2010 <= int(line['iyr']) <= 2020:
            continue
        if not 2020 <= int(line['eyr']) <= 2030:
            continue
        if line['hgt'].endswith('cm'):
            if not 150 <= int(line['hgt'][:-2]) <= 193:
                continue
        elif line['hgt'].endswith('in'):
            if not 59 <= int(line['hgt'][:-2]) <= 76:
                continue
        else:
            continue
        if not re.fullmatch(r'#[0-9a-f]{6}', line['hcl']):
            continue
        if line['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if not re.fullmatch(r'[0-9]{9}', line['pid']):
            continue

        cnt += 1


    print(cnt)
