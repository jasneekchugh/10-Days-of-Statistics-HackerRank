import math

#definied function 'binomial' to calculated using binomial experiment formula
def binomial(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b=0

p=1.09/2.09 #p= prob of success
n= 6 #n= total no of trials
for i in range(3,7):
    b += binomial(i, n, p)   
print(round(b,3))
