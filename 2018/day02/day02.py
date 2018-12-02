print("Hallo day02!")

def parseString(s):
    #print(s)
    global cnt2s, cnt3s

    charList = []
    for c in s:
        found = False
        for e in charList:
            if(e[0] is c):
                e[1] = e[1] + 1
                found = True
        if(found is False):
           # print("Append" + c)
            charList.append([c, 1])

    charList.sort()
    found2 = False
    found3 = False
    for e in charList:
        if(e[1] is 2):
            print("Found a 2, it is: " + e[0])
            found2 = True
        if(e[1] is 3):
            print("Found a 3, it is: " + e[0])
            found3 = True

    if(found2 is True):
        cnt2s = cnt2s + 1

    if(found3 is True):
        cnt3s = cnt3s + 1

    print("2s: " + str(cnt2s) + " and 3s: " + str(cnt3s))


def diffString(d, s):
    #print(s)

    for idx in d:
        checkCnt = 0
        for i, c in enumerate(s):
            if(idx[i] is c):
                checkCnt = checkCnt + 1
        if (checkCnt is (len(s) - 1)):
            print(s + " " + idx)


    #print(checkCnt)

cnt2s = 0
cnt3s = 0


testString = "nkucgflarhzwsijroevymbdpoq"
#parseString(testString)

data = open('input02.txt', 'r').read().splitlines()

#for idx in data:
#    parseString(idx)

for idx in data:
    diffString(data, idx)

