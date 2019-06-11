import time
import math
Factorials = []
Digit_Factorials = []
start = time.time()

def factorial_generator(lower_bound,upper_bound):
    for x in range(lower_bound,upper_bound+1):
        Factorials.append(math.factorial(x))

factorial_generator(1,9)

def Digit_factorials_3digits(lower_bound,upper_bound,x,a,b,c):
    while x > upper_bound:
        x = Factorials[a] + Factorials[b] + Factorials[c]

Digit_factorials(144,1000,100,0,0,0)
print(sum(Digit_Factorials))
end = time.time()
print(end - start)