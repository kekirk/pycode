#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyecharts import Scatter3D
import numpy as np


# # 心形解析式

# # (x^2+9/4*y^2+z^2-1)^3-x^2*z^3-9/80*y^2*z^3=0

# In[5]:


scatter3D = Scatter3D("I Love You", width=1700, height=1000)
data = list()
x = list(np.linspace(-1.5, 1.5,150))
y = list(np.linspace(-1,1,100))
z = list(np.linspace(-1.5,1.5,100))

for a in x:
    for b in y:
        for c in z:
            if -0.05<=(a**2+9.0/4.0*b**2+c**2-1)**3-a**2*c**3-9.0/80.0*b**2*c**3 <=0:
                data.append([a,b,c])
scatter3D.add("", data, is_visualmap=True, visual_range_color="red")
scatter3D.render()
scatter3D


# In[20]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




