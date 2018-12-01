#! /usr/bin/python

print("Hello 2018, Day1")

data = open('input01.txt', 'r').read().splitlines()

len = len(data)

list = []

print("Len: " + str(len))

sum = 0

list.append(sum)

for x in range(0, 300):
    for val in data:
        sum = sum + int(val)
        if(sum in list):
            print("Found something!: " + str(sum))
        list.append(sum)
