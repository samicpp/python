print("enter a comma sepperated list of ints")
csv=input("")

l=csv.split(",")
b=0
for i in l:
    if(int(i)>b):b=int(i)

print(f"largest integer is {b}")