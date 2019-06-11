#since 10^n grows much faster than n*9!
#d(n*9!)/dn is a constant (9!) while d(10^n)/dn = (10^n)*ln(10)
#there are clearly no sinlge or double digit factorials apart from 1 and 2 since since 3! neq 6  and 4! > 9.
#5! > 99. So if there is a double digit factorial, then its bounded from below by 10 and above by 44.
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
