# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

size = int(input())
numbers = list(map(int, input().split()))

def mean(data):
    return sum(data) / len(data)

def stddev(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / size)

print(round(stddev(numbers, size), 1))