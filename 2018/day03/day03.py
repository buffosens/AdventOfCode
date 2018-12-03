print("Hallo day03!")


maxW = 0
maxH = 0

def overLapCheck(input):
    s = input.split(" ")

    s[2] = s[2][:-1]

    s2 = s[2].split(",")

    x = s2[0]
    y = s2[1]

    s3 = s[3].split("x")

    w = s3[0]
    h = s3[1]

    found = True

    for i in range(int(w)):
        for j in range(int(h)):
            coordx = int(x) + i
            coordy = int(y) + j
            # print(coordx)
            # print(coordy)

            # print(str(coordx) + " " + str(coordy) )
            # print(str(coordx) + " " + str(coordy))
            if(mymap[coordx][coordy] is not 1):
                found = False

    if(found is True):
        print("Got one!")
        print(input)



def parseMapInput(input):
    s = input.split(" ")

    s[2] = s[2][:-1]

    s2 = s[2].split(",")

    #print(s2)

    x = s2[0]
    y = s2[1]

    s3 = s[3].split("x")

    #print(s3)

    w = s3[0]
    h = s3[1]

    for i in range(int(w)):
        for j in range(int(h)):
            coordx = int(x) + i
            coordy = int(y) + j
            # print(coordx)
            # print(coordy)

            # print(str(coordx) + " " + str(coordy) )
            # print(str(coordx) + " " + str(coordy))
            mymap[coordx][coordy] = mymap[coordx][coordy] + 1


a = 1000
b = 1000


cnt = 0

mymap = [[0 for xx in range(a)] for yy in range(b)]

data = open('input03.txt', 'r').read().splitlines()

#test = "#1 @ 829,837: 11x22"
#parseMapInput(test)
#parseMapInput(test)

for idx in data:
    parseMapInput(idx)

    overLapCheck

for i in range(int(a)):
    for j in range(int(b)):
        if mymap[i][j] > 1:
            #print("Found entry here: " + str(i) + " " + str(j))
            cnt = cnt + 1

for idx in data:
    overLapCheck(idx)




