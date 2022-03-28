import random 
from time import time

def mysort(L):
    if len(L)==1:
         return L
    elif len(L)==2:
        if L[0]>L[1]:
            return [L[1],L[0]]
        else:
            return L              
    left=L[:len(L)//2]
    left=mysort(left)
    right=L[len(L)//2:]
    right=mysort(right)
    res=[]
    while len(right)>0 and len(left)>0:
        if right[0]>left[0]:
            res.append(left[0])
            left=left[1:]
        else: 
            res.append(right[0])
            right=right[1:]
    res+=right
    res+=left
    return res  

           



items=20
lst=[random.randrange(1000) for i in range(items)]
random.shuffle(lst)
ts=time()
print(lst)  
print(mysort(lst))
print(time()-ts)           