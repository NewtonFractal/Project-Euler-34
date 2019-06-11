import time
import math
Factorials = []
Digit_Factorials = []
start = time.time()

def factorial_generator(lower_bound,upper_bound):
    for x in range(lower_bound,upper_bound+1):
        Factorials.append(math.factorial(x))

factorial_generator(1,9)

def Digit_factorials(lower_bound,upper_bound):
    for x in range(lower_bound,upper_bound+1):
        for y in Factorials:
            for z in Factorials:
                if y + z == x:
                    Digit_Factorials.append(x)
                if y + z > x:
                    break

Digit_factorials(144,2540160)

end = time.time()
print(end - start)
