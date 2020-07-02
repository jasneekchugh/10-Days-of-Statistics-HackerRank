#Normal Distribution 1

import math

initial_input = list(map(float, input().split()))
mean = initial_input[0]
std = initial_input[1]
less_period = float(input())
between_period = list(map(float, input().split()))

def cumulative(mean, std, val):
    return ((1/2) * (1 + math.erf((val - mean) / (std * math.pow(2,0.5)))))

ans_1=cumulative(mean, std, less_period)
ans_2=cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0])

print (round(ans_1,3))
print (round(ans_2, 3))

