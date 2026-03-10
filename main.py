import math
x = float(input("1-sonni kiriting "))
y = float(input("2-sonni kiriting "))
a = math.pow(y , 2) + (y + x * y) / (math.fabs(x * y) + 5)
b = math.pow(x , 2) + (x * y + math.pow(y , 2)) / a 
c = (math.pow(x , 2) + 1) / b
d = 1 / (1 + math.cos(x) + (1 /math.sin(x)))
t11 = c + d
print("%.2f" % 2)