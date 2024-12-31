a = 20256
b = 37589
c = a*b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(c//a)
