namen='''Damini Boedhoe
Eren Çoskun
Mark de Vries
Rihab El Arkoubi
Azad Hemidli
extra waarde1
extra waarde2'''.split("\n");

namen[3]="Piet"

for n in range(3):print(namen[n])

print("\n")#line sepperator

for n in namen:print(n)

print("\n")#line sepperator

namen2=namen

for a in namen2[::-1]:print(a)