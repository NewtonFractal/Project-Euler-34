import time
import math

Factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
Digit_Factorials = []
start = time.time()


def Digit_factorials_3digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(Factorials[int(x[0])]) + int(Factorials[int(x[1])]) + int(Factorials[int(x[2])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[2] == "7":
            x = str(int(x)+3)
        if x[1] == "7":
            x = str(int(x)+30)


Digit_factorials_3digits(str(100), 600)


def Digit_factorials_4digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(Factorials[int(x[0])]) + int(Factorials[int(x[1])]) + int(Factorials[int(x[2])]) + int(
                Factorials[int(x[3])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[2] == "8":
            x = str(int(x)+20)
        if x[1] == "8":
            x = str(int(x)+200)
        if x[3] == "8":
            x = str(int(x)+2)

Digit_factorials_4digits(str(1000), 7201)

def Digit_factorials_5digits(x, upper_bound):
    while int(x) < upper_bound:
        if str(x) == str(int(Factorials[int(x[0])]) + int(Factorials[int(x[1])]) + int(Factorials[int(x[2])]) + int(Factorials[int(x[3])])+int(Factorials[int(x[4])])):
            Digit_Factorials.append(int(x))
            x = str(int(x) + 1)
        else:
            x = str(int(x)+1)
        if x[3] == "9":
            x = str(int(x)+10)
            if x[2] == "9":
                x = str(int(x)+100)
                if x[1] == "9":
                    x = str(int(x)+1000)


Digit_factorials_5digits(str(10000), 95760)

print(Digit_Factorials)
end = time.time()
print(end - start)
