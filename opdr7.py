print("note the hight of the triangle and the width sepperated by a comma")
wh=input("")

ws,hs=wh.split(",")
print(f"calculating with and height of width {ws} and height {hs}")

w=float(ws.strip())
h=float(hs.strip())

print(f"volume is {w*h/2}")
