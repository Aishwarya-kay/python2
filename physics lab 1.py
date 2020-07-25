#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=1000345
count=0
while num!=0:
    num //=10
    count+=1 
print("totalcounts are:", count)


# In[20]:


#Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if (i %5 ==0):
        print(i)
    if (i>=150):
        break


# In[ ]:




