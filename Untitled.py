#!/usr/bin/env python
# coding: utf-8

# In[17]:


print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")


# In[21]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[22]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[23]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[24]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[27]:


val1 = int(input("enter your value 1"))


# In[29]:


val2 = int(input("enter your value 2"))


# In[30]:


val3 = val1 + val2


# In[31]:


print(val3)


# In[35]:


mark_1= int(input("enter your mark 1"))
mark_2 = int(input("enter your mark 2"))
mark_3 = int(input("enter your mark 3"))
mark_4 = int(input("enter your mark 4"))
mark_5 = int(input("enter your mark 5"))
total_mark = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5)*100/500
print(total_mark)


# In[43]:


num = int(input("enter your value"))
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[44]:


ListName = ["Hello", "Edureka", 1, 2, 3]
print ("Number of items in the list = ", len(ListName))


# In[46]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[47]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# In[60]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i >=5:
        continue
# print(a)
print(i)
    
    


# In[ ]:




