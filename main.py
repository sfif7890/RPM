import math

print("ax^2 + bx + c = 0")
a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите c "))
d = (b**2) - (4*a*c)

def answer():
    otvet = ((b*-1)+ d) / (2*a)
    print("x = ", + otvet)

if d < 0:
    print("Нет ответа")
if d >= 0 :
    d = math.sqrt(d)
if d == 0:
    answer()
if d > 0:
    answer()
    d = d * -1
    answer()
