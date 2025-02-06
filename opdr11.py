i=int(input("how many:").strip())

while(i!=0):
    r=""
    for l in range(i):
        r+="*"
    print(r)
    i-=1
