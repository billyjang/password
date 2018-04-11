import hashlib
import codecs
#OHH repeated calls to update are concatenations of the string.
#how to get new md5
#how to get two files in
#list comp or lambda for generating hex list

def main():
    #print(genHashedRawList())
    #print(genHashList())
    checkPassword()

def checkPassword():
    #rawWords = genRawList()
    #hashedUserWord = genHashedRawList()
    hashedPass = genHashList()

    with codecs.open('xac', mode='r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            s = word.encode('utf-8')
            m = hashlib.md5()
            m.update(s)
            digest = m.hexdigest()
            if digest in hashedPass:
                print(word)
    f.closed

    '''
    hashcount = 0
    for userWord in hashedUserWord:
        if userWord in hashedPass:
            print(str(rawWords[hashcount]))
        hashcount = hashcount + 1
    '''

#opens the file of raw passwords and returns a list

'''
def genRawList():
    rawlines = []
    with codecs.open('naxx.txt', 'r', encoding='utf-8', errors = 'ignore') as f:
        rawlines = f.readlines()
        rawlines = [line.strip() for line in rawlines]
    f.closed
    return rawlines
'''


#opens the file of hash passwords and returns a list
def genHashList():
    hashline = ""
    with open('moderate.txt') as h:
        for l in h:
            hashline = hashline + l
    h.closed
    hashlines = hashline.split()
    hashlines = hashlines[1::2]
    hashlines_set = hashlines
    return hashlines

'''
def genHashedRawList():
    rawlines = genRawList()
    hashedRawLines = []

    for l in rawlines:
        s = l.encode('utf-8')
        m = hashlib.md5()
        m.update(s)
        hashedRawLines.append(m.hexdigest())
    
    return hashedRawLines
'''

def createBinaryTree():
    return 0


if __name__ == "__main__": main()

