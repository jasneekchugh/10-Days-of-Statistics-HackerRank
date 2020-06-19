
size=int(input())
numbers=sorted(list(map(int,input().split())))

from statistics import median
print(int(median(numbers[:size//2]))) #Q1
print(int(median(numbers)))#Q2
print(int(median(numbers[(size+1)//2:])))#Q3


#map: Return an iterator that applies function to every item of iterable, yielding the results.
#sorted: Return a new sorted list from the items in iterable.

#We can avoid using list() here.
#Hence list does not have to be called. Rather calling it will slow down your program 
#since the whole list will be created in memory before being sorted. sorted will then 
#create another list after which the first list will be removed by GC. All this can be 
#avoided if you directly call sorted after map.