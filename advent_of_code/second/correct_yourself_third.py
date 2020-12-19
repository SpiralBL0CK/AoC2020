import re
def s():
    z = 0
    i = 0
    f = open("input","r")
    for line in f.readlines():
        mina = int((line).split()[0].split('-')[0])
        #print((line).split()[0].split('-')[0])
        maxa = int((line).split()[0].split('-')[1])
        letter = line.split()[1].split(":")[0]
        text = line.split()[2]
        
        chara = text[mina-1]
        charb = text[maxa-1]
        if(mina <= len(re.findall(letter, text)) <= maxa ):
            i+=1
        
        if(text[mina-1] == letter) ^ (text[maxa-1] == letter):
            z +=1
    print(z)
    

if __name__ == "__main__":
    s()

