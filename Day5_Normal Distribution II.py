#Normal Distribution II

import math

initial_input = list(map(float, input().split()))
mean = initial_input[0]
std = initial_input[1]
grade_1 = float(input())
grade_2 = float(input())

def cumulative(mean, std, val):
    return ((1/2) * (1 + math.erf((val - mean) / (std * math.pow(2,0.5)))))

print (round(100 - (cumulative(mean, std, grade_1) * 100), 2))
print (round(100 - (cumulative(mean, std, grade_2) * 100), 2))
print (round(cumulative(mean, std, grade_2)* 100, 2))
