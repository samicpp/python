def som(x:float=1,y:float=2)->float:
    return x+y

i=input(":")
try:
    i=float(i)
except:
    print("couldnt parse")

print(som(x=i,y=i))