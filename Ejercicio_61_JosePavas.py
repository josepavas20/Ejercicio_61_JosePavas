import random


nombre=input("ingrese su nombre")
edad=int(input("ingrese su edad"))

def area ():
    radio=int(input("ingrese el radio del circulo"))
    return 3.14*radio**2

print(area())


num=random.randint(0,10000)
print(num)


numero=int(input("ingrese el numero"))
if numero % 2 == 0:
    print("el numero", numero ,"es par")
else:
    print("el numero", numero ,"es impar")


def grados ():
    grados_fahrenheit=float(input("ingrese los grados fahrenheit"))
    return grados_fahrenheit-32

print(grados())

