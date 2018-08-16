
# coding: utf-8

# In[2]:

name = "superman"


# In[3]:


age =9


# In[4]:


print(name)


# In[5]:


print(age)


# In[6]:


print("my name is")


# In[7]:


print("my name is", name)


# In[8]:


print("my age is", age)


# In[10]:


print("my name is", name, "and my age is", age)


# In[11]:


newage = age - 50


# In[12]:


multipledage = age*2


# In[13]:


print("your age is actually", newage)


# In[16]:


print("your multiplied age is",multipledage)


# In[17]:


NewAge = 100


# In[19]:


sequence = "CTAGCTAG"


# In[20]:


print(sequence)


# In[21]:


print(sequence[0])


# In[22]:


print(sequence[3])


# In[23]:


print("my fourth letter is", sequence[3])


# In[24]:


len(sequence)


# In[26]:


print("the length of the sequence is", len(sequence))


# In[37]:


COX1 = "CTAG"


# In[27]:


first_name = "anuj"


# In[28]:


sequence[0:2]


# In[29]:


sequence[0:3]


# In[30]:


type(sequence)


# In[31]:


type(age)


# In[32]:


COX2 = "TACG"


# In[39]:


COX1 - COX2


# In[38]:


COX1 + COX2


# In[40]:


firstname = "anuj"


# In[41]:


lastname = "guru"


# In[44]:


firstname + " " + lastname


# In[45]:


age


# In[46]:


len(age)


# In[47]:


name + age


# In[48]:


5**2


# In[49]:


print(5**2)


# In[50]:


print ("5 square is", 5 **2)


# In[51]:


5%2


# In[ ]:


# this is a comment


# In[52]:


COX1 + COX2


# In[53]:


max (23, 2,5)


# In[54]:


max (3, "anuj")


# In[55]:


round(3.1415926)


# In[56]:


round(3.1415926,2)


# In[57]:


min(2,3,4)


# In[58]:


help(min)


# In[59]:


help(round)


# In[60]:


max(21,32,45) + min(21, 32,45)


# In[61]:


hundred_C = "c" * 100


# In[62]:


100_C = "c"*100


# In[63]:


print(hundred_C)


# In[64]:


hundred_C + COX1


# In[65]:


len(hundred_C + COX1)


# In[66]:


import math


# In[67]:


math.cos(180)


# In[68]:


math.sin(180)


# In[69]:


math.sin(3.14)


# In[70]:


print("the sine of 180 is", math.cos(180))


# In[71]:


math.pi


# In[72]:


math.sin(math.pi)


# In[73]:


math.cos(math.pi)


# In[74]:


help(math)


# In[75]:


import math as m


# In[76]:


m.cos(45)


# In[77]:


from math import cos


# In[78]:


cos(45)


# In[79]:


from math import sin,pi
print("sin(pi/2)=",sin(pi/2))


# In[80]:


import math as m
print("sin(pi/2)=",m.sin(m.pi/2))


# In[81]:


import math
math.sin(math.pi/2)


# In[82]:


from math import *
sin(pi/2)


# In[83]:


from math import degrees, pi
angle = degrees (pi/2)
print(angle)


# In[84]:


import pandas


# In[85]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[87]:


pandas.read_csv ("data/gapminder_gdp_americas.csv")


# In[88]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[89]:


print(data)


# In[90]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv", index_col = "country")


# In[91]:


data


# In[92]:


data.info()


# In[93]:


data.T


# In[94]:


data.describe()


# In[95]:


data.T.describe()


# In[102]:


americas = pandas.read_csv("data/gapminder_gdp_americas.csv",index_col="country")


# In[104]:


americas.describe()


# In[105]:


data.columns


# In[106]:


americas.columns


# In[107]:


data.iloc[1,2]


# In[108]:


data.iloc[0,0]


# In[109]:


data.loc["Australia","gdpPercap_1952"]


# In[110]:


data.loc["Australia",:]


# In[113]:


data.loc[:,"gdpPercap_1952"]


# In[114]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[116]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"]


# In[117]:


data.iloc[0,0:3]


# In[118]:


data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"].max()


# In[119]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].max()


# In[120]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].min()


# In[121]:


subset = data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[122]:


print(subset > 11000)


# In[123]:


subset[subset > 11000]


# In[124]:


subset[subset > 11000].describe()


# In[126]:


europe = pandas.read_csv("data/gapminder_gdp_europe.csv",index_col="country")


# In[128]:


europe.loc["Serbia","gdpPercap_2007"]


# In[129]:


subset2 = europe.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]
subset2 < 15000


# In[130]:


subset2[subset2 < 15000].describe()

