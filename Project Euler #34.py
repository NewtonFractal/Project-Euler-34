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
            for z in factorials:
                if y + z == x:
                    Digit_Factorials.append(x)

Digit_factorials(144,2903040)

end = time.time()
print(end - start)