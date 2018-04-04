import hashlib
#OHH repeated calls to update are concatenations of the string.
#how to get new md5
#how to get two files in
#list comp or lambda for generating hex list

def main():
    #print(genHashedRawList())
    #print(genHashList())
    checkPassword()

def checkPassword():
    rawWords = genRawList()
    hashedUserWord = genHashedRawList()
    hashedPass = genHashList()

    count = 0
    for userWord in hashedUserWord:
        hashcount = 1
        for hashed in hashedPass:
            if userWord == hashed:
                print(str(hashcount) + ": " + rawWords[count])
            hashcount = hashcount + 1
        count = count + 1

#opens the file of raw passwords and returns a list
def genRawList():
    rawlines = []
    with open('weak.txt') as f:
        rawlines = f.readlines()
        rawlines = [line.strip() for line in rawlines]
    f.closed
    return rawlines

#opens the file of hash passwords and returns a list
def genHashList():
    hashline = ""
    with open('weak.txt') as h:
        for l in h:
            hashline = hashline + l
    h.closed
    hashlines = hashline.split()
    hashlines = hashlines[1::2]
    return hashlines

def genHashedRawList():
    rawlines = genRawList()
    hashedRawLines = []

    for l in rawlines:
        s = l.encode('utf-8')
        m = hashlib.md5()
        m.update(s)
        hashedRawLines.append(m.hexdigest())
    
    return hashedRawLines

def createBinaryTree():
    return 0


if __name__ == "__main__": main()

