print("Hallo day05!")

data = open('input05.txt', 'r').read().splitlines()

list = []

def parseString(s, c):
    for h in range(2000):
        for j in range(26):
            s = s.replace(str(reactions[j]), "")

        for j in range(26):
            s = s.replace(str(Reactions[j]), "")

    for i in range(26):
        if (s.find(reactions[i]) is not -1):
            print(" -->" + s.find(reactions[i]))
        if (s.find(Reactions[i]) is not -1):
            print(" -->" + str(s.find(Reactions[i])))

    print(str(len(s)) + " " + c)

Reactions = [0 for xx in range(26)]
reactions = [0 for xx in range(26)]

cnt = 0
for i in range(65, (65+26)):
    Reactions[cnt] = str(chr(i)) + str(chr(i+32))
    cnt = cnt + 1

cnt = 0
for i in range(65, (65+26)):
    reactions[cnt] = str(chr(i+32)) + str(chr(i))
    cnt = cnt + 1

parseString(data[0], 'a')

test = "abAcCaCBAcCcaA"

for l in range(65, (65+26)):
    temp = data[0]
    #temp = "dabAcCaCBAcCcaDA"
    temp = temp.replace(str(chr(l)), "")
    #print(chr(l))
    temp = temp.replace(str(chr(l+32)), "")
    parseString(temp, str(chr(l)))
    print(temp)



