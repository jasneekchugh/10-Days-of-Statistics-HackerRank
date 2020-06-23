import math as m

p=0
p1=0
for i in range(10):
    if (i<=2):
        p+=m.factorial(10)/(m.factorial(10-i)*m.factorial(i))*(0.12**i)*(0.88**(10-i))
    if(i>=2):
        p1+=m.factorial(10)/(m.factorial(10-i)*m.factorial(i))*(0.12**i)*(0.88**(10-i))
print(round(p,3))
print(round(p1,3))