import math

print("ax^2 + bx + c = 0")
a = int(input("write a "))
b = int(input("write b "))
c = int(input("write c "))
d = (b**2) - (4*a*c)
otvet = int

def answer():
    global otvet
    otvet = ((b*-1)+ d) / (2*a)
    print("x = ", + otvet)

if d < 0:
    print("no answer")
d = math.sqrt(d)
if d == 0:
    answer()
if d > 0:
    answer()
    d = d * -1
    answer()
