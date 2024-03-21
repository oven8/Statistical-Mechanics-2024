import pandas as pd
import numpy as np
from math import *

d = pd.read_csv("/home/thakkar/Downloads/Turkish.csv")
bd = pd.read_csv("/home/thakkar/Downloads/Bigram_Turkish.csv")

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
out = [0]*len(alp)

for i in range(len(alp)):
    for j in range(np.shape(bd)[0]):
        if bd.iloc[j,0][0] == alp[i]:
            k = alp.index(bd.iloc[j,0][1])
            out[i] += float(bd.iloc[j,1])*float(d.iloc[k,1])
"""
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
"""



