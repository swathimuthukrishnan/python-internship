#!/usr/bin/env python
# coding: utf-8

# In[41]:


#movie problem
yes="yes"
no="no"
a=input("is magna alive")
if(a==yes):
    print("surya did not marry priya")
elif(a==no):
    print("suriya married priya")


# In[42]:


#odd or even
a=int(input("enter a value 1"))
if(a%2==0):
    print("number is even")
else:
    print("number is even")



# In[43]:


#calculator
a=int(input("enter a 1st value"))
b=int(input("enter a 2nd value"))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a//b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


# In[44]:


#traiangle
a=int(input("value of 1st side"))
b=int(input("value of 2st side"))
c=int(input("value of 3st side"))
if(a+b>c and a+c>b and b+c>a):
    if(a==b==c):
        print("it's a equilateral")
    elif(a==b or b==c or c==a):
        print("it is a isoscales")
    elif(a!=b!=c):
        print("it is a scalene")
else:
        print("not a valid triangle")


# In[68]:


#income
a=int(input("enter a income"))
if(a>=7000):
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")


# In[66]:


#factorial
for a in range (6,9):
    print((a-1)*a)


# In[73]:


#loan eligiblity
a=int(input("enter a salary"))
b=int(input("enter age"))
if(a>=20000 or b<=25):

    c=int(input("enter a amount required"))
    if(c<=500000):
        print("your eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible for loan")


# In[77]:


#divisible by 3 and 5
a=int(input("enter a value"))
if(a//3 and a//5):
    print("the number is divisible by 3 and 5")
else:
    print("the number is not divisible by 3 and 5")


# In[4]:


#odd and even between 1 to 10
odd_count = 0
even_count = 0
for i in range(1, 11):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd numbers:", odd_count)
print("Even numbers:", even_count)


# In[13]:


#STAR 
n = int(input("Enter the number of rows: "))
for i in range(n):
    print("* " * n)


# In[ ]:




