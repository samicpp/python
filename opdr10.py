getallen1=[0,0,0]#reserve pos

print("voer 3 komma onderscheden nummers")
numstr=input(": ").split(",")
for n in range(3):getallen1[n]=int(numstr[n].strip())

getallen2=[2,9,15]
getallen3=[0,0,0]

for n in range(3):getallen3[n]=getallen1[n]+getallen2[n]

for n in getallen3:print(n)