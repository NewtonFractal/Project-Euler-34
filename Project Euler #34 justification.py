#since 10^n grows much faster than n*9!
#d(n*9!)/dn is a constant (9!) while d(10^n)/dn = (10^n)*ln(10)
import time
import math

start = time.time()
Loop = True
x = math.factorial(9)
y = 1
while Loop == True:
    if y > x:
        Loop = False
        break
    x += math.factorial(9)
    y *= 10

print(len(str(x)))
print(len(str(y)))
print(x)
print(y)
print(7*math.factorial(9))

end = time.time()
print(end - start)
