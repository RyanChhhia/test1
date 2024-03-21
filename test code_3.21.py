# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:47:20 2024

@author: 不会流泪的鱼
"""

print("Hello World")

a = 1
b = a+1
print(b)

import numpy as np

g = np.array([6,2,1])
A = np.array([[1,1,0,0,0], [1,1,1,1,0], [0,0,2,0,3]])
# 先行后列，记得加大括号！
c = np.array([1,2,5,3,8])
r = np.dot(g,A).dot(c)
print(r)

