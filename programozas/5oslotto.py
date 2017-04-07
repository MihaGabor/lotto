import random 
a = []
x = random.randrange(1,91)
while len(a)<5:
    if x not in a:
        a.append(x)