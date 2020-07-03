#Central Limit Theorem III
import math

n = float(input())
mean = float(input())
std = float(input())
interval = float(input())
z = float(input())

#m=margin of Error
m = z * (std / math.sqrt(n))

print(round(mean - m, 2))
print(round(mean + m, 2))