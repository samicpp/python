print("lever een aantal getallen onderscheid met een komma `,`")
csv=input(": ")

l=csv.split(",")
b=0
for i in l:
    if(int(i)>b):b=int(i)

print(f"grootste nummer is {b}")