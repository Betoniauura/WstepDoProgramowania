"""
n = int(input("Proszę podać liczbę studentów: "))
a = 1 #wyświetlanie od 1 studenta
c = 0
 #podstawienie pod dodawanie punktów
while True:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    if b<0 or b>100:
        continue
        c += b
        a += 1
        if a == n+1:
            break
y = c/n
print("Średnia wszystkich studentów",y)

for i in range(100,-1,-10):
    print(i)

b = int(input("Podaj wyskokośćS:"))
for i in range(b):
    for i in range(b):
          print("*",end="")
print()

x = ["Jajka","Mleko","Śmietana","Mąka","CocaCola"]

print(x)
print(x[0],x[1])

x[2]="mleko"
print(x)
print(x[-1],x[-2])

import random

zestaw_1 = []
a = int(input("Podaj ilość elementów listy"))
for i in range(a):
    x = random.randint(1,10)
    zestaw_1.append(x)
print(zestaw_1)



x = [1,2,3,4,5,6,]
a = int(input("Wprowadź liczbę"))
if a in x:
    print("lol")
else:
    print("lpl")


x = [1,2,3,4,5,6,]
d = [8,9,7]
zestaw_1_2 = x + d
zestaw_1_2.sort()
print(zestaw_1_2)



import random
punkty=[]
for x in range(15):
    punkty.append(round(random.uniform(0,50),2))
print(punkty)
"""


