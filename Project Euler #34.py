
import time
import math
Factorials = [1,1,2,6,24,120,720,5040,40320,362880]
Digit_Factorials = []
start = time.time()

def Digit_factorials_3digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(Factorials[int(x[0])])+int(Factorials[int(x[1])])+int(Factorials[int(x[2])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) +1)
        else:
            x = str(int(x)+1)
        if x[2] == "7":
            x = str(int(x)+4)
        if x[1] == "7":
            x = str(int(x)+40)

Digit_factorials_3digits(str(100), 600)
print((Digit_Factorials))
end = time.time()
print(end - start)
