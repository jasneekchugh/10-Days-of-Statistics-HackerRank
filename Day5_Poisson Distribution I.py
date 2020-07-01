import math

def poisson(λ, k):
    return (math.pow(λ,k) * math.pow(math.e,(-λ)) / math.factorial(k))

λ = float(input())
k = int(input())

print(round(poisson(λ, k)),3)