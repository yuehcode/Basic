#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(N):
    N = str(bin(N)[2:])
    count = False
    gap = 0
    maxgap = 0
    for i in N:
        if i == '1' and count==False:
            count = True
        if i == '0' and count == True:
            gap += 1
        if i == '1' and count == True:
            maxgap = max(maxgap, gap)
            gap = 0
    return maxgap

