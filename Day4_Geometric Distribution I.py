#1

import math

nd = list(map(int, input().split()))
p = nd[0] / nd[1]
q = 1 - p
n = int(input())

result = math.pow(q,(n - 1)) * p
print(round(result, 3))

#2
import math

p=1/3
n=5
result=math.pow(q,(n - 1)) * p
print(round(result, 3))