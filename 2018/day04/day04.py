import datetime

state = 0
guardInfo = ""
asleep = ""
wakeUp = ""
cnt = 0

aa = 62
bb= 300

mymap = [[0 for xx in range(aa)] for yy in range(bb)]

def getState(s):
    global state
    if("begins shift" in s):
        state = 0
    elif("falls asleep" in s):
        state = 1
    elif("wakes up" in s):
        state = 2
    else:
        assert(0)


def parseTimeInput(s):
    global state, asleep, wakeUp, guardInfo, cnt
    getState(s)

    if(state is 0):
        #get guard info
        intro = s.split(" ")
        guardInfo = intro[3]
        #print(intro[3])
    if(state is 1):
        asleep = s[1:17]
    if(state is 2):
        wakeUp = s[1:17]

        a = datetime.datetime.strptime(asleep, '%Y-%m-%d %H:%M')
        b = datetime.datetime.strptime(wakeUp, '%Y-%m-%d %H:%M')

        diff = b - a
        #print(a)

        min = diff.seconds / 60

        # print(str(a.minute) + " " + str(b.minute) + " " + str(min))

        found = False
        index = 0

        for j in range(bb):
            if(mymap[j][0] == guardInfo):
                for i in range(int(min)):
                    mymap[j][a.minute + i + 1] = mymap[j][a.minute + i + 1] + 1
                    if(mymap[j][a.minute + i + 1] > 18):
                        #print(guardInfo + " " + str(a.minute + i + 1))
                        print("Part 2: " + str(int(guardInfo[1:]) * int((a.minute + i + 1) - 1)))
                found = True

        if(found is False):
            for i in range(int(min)):
                 mymap[cnt][0] = guardInfo
                 mymap[cnt][a.minute + i + 1] = mymap[cnt][a.minute + i + 1] + 1

            cnt = cnt + 1

print("Hallo day04!")

data = open('input04.txt', 'r').read().splitlines()

data.sort()

for idx in data:
    parseTimeInput(idx)

for i in range(bb):
    for j in range(1, aa):
        mymap[i][61] = mymap[i][61] + mymap[i][j]

maxMin = 0
wantedIdx = 0
for k in range(bb):
    if(mymap[k][61] > maxMin):
        maxMin = mymap[k][61]
        wantedIdx = k

wantedMin = 0
wantedMinIdx = 0
for l in range(1, aa - 1):
    if(mymap[wantedIdx][l] > wantedMin):
        wantedMin = mymap[wantedIdx][l]
        wantedMinIdx = l

print("Part 1: " + str(int(mymap[wantedIdx][0][1:]) * (wantedMinIdx - 1)))




