# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:52:48 2016

@author: Zi
"""
##Multiples of 3 and 5
n3=0
n5=0
for i in range(1000):
    if i%3==0:
        n3+=i
    if i%5==0 and i%3!=0:
        n5+=i
print n3+n5

#Even Fibonacci numbers
lists=[1,2]
i=0
t=0
while(t<4000000):
    t=lists[i]+lists[i+1]
    i+=1
    lists.append(t)
sums=0
for x in lists:
    if x%2==0:
        sums+=x
print sums

##Largest prime factor
from math import sqrt
def is_prime(n):                                            
    list_num = []    
    for i in range(2, n):        
        for num in range(2, int(sqrt(n))+1):            
            if i % num == 0 and i != num:                
                break            
            elif i % num != 0 and num == int(sqrt(n)):                
                list_num.append(i)    
    return list_num
    
##Largest palindrome product     
l=[]
for i in range(101,1001):
   for j in range(101,1001):
      s=i*j
      list1=list(str(s))
      list2=list(str(s))
      list2.reverse()
      if list1==list2:
         l.append(s)
max(l)