import time
import math
Factorials = []
Digit_Factorials = []
start = time.time()

def factorial_generator(lower_bound, upper_bound):
    for x in range(lower_bound, upper_bound + 1):
        Factorials.append(math.factorial(x))


factorial_generator(1, 9)

def Digit_factorials_3digits(x, upper_bound):
    while int(x) < upper_bound:
        x = str(x)
        if str(x) == str(Digit_Factorials[int(x[0])-1]):
            Digit_Factorials.append(x)

Digit_factorials_3digits(100, 600)
print((Digit_Factorials))
end = time.time()
print(end - start)
