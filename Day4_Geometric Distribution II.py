import math

nd = list(map(int, input().split()))
p = nd[0] / nd[1]
q = 1 - p
n = int(input())
# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (math.pow(q, (i - 1)) * p)
print(round(result, 3))