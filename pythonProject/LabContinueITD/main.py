'''
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
'''

x = []
a = int(input("Podaj ilość elementów listy"))
import random
k = random.randint(1,10)

x.append(k)
print(x)
