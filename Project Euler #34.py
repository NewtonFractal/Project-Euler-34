import time
import math
Factorials = []
Digit_Factorials = []
start = time.time()

def factorial_generator(lower_bound,upper_bound):
    for x in range(lower_bound,upper_bound+1):
        Factorials.append(math.factorial(x))

factorial_generator(1,9)

def Digit_factorials_3digits(x,a,b,c):
    while c < 5:
        if x == Factorials[a] + Factorials[b] + Factorials[c]:
            Digit_Factorials.append(x)
        if a != 5:
            a += 1
        else:
            b += 1
            a = 0
        if b == 5:
            c += 1
            b = 0
        if c == 5:
            x += 1
            c = 0
            if x == 999:
                break


Digit_factorials_3digits(100,0,0,0)
print((Digit_Factorials))
end = time.time()
print(end - start)
