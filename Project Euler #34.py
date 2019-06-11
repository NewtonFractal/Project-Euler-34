import time
import math
Factorials = []
Digit_Factorials = [1,1,2,6,24,120,720]
start = time.time()

def Digit_factorials_3digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(Digit_Factorials[int(x[0])-1]+Digit_Factorials[int(x[1])-1]):
            Digit_Factorials.append(x)
        else:
            x = int(x) + 1
        x = str(x)
        if x[2] == "7":
            x = str(int(x)+4)
        if x[1] == "7":
            x = str(int(x)+40)

Digit_factorials_3digits(str(100), 600)
print((Digit_Factorials))
end = time.time()
print(end - start)
