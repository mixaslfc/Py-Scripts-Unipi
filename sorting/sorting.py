import random
from time import time
items=10000
lst=[random.randrange(1000) for i in range(items)]
# lst=['petros',"george",'johan','carol','alister','bob']
random.shuffle(lst)
lst=lst[::-1]
ts=time()
cnt=0
for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
        cnt+=1
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(time()-ts)
