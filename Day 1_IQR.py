# Enter your code here. Read input from STDIN. Print output to STDOUT

import statistics as st

size = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(size):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if size%2 != 0: #IF Size is ODD
    q1 = st.median(s[:N//2])
    q3 = st.median(s[(N//2)+1:])
    
else: #If Size is EVEN
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

IQR = round(float(q3-q1), 1)
print(IQR)