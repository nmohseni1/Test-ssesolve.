
# coding: utf-8

# In[7]:


import time 
import argparse
import numpy as np
from qutip import *
from math import sqrt
from scipy import *
from scipy.special import factorial
import matplotlib.pyplot as plt
import pandas as pd
N = 4
T = 6.
gamma = 0.25
ntraj = 25
nsubsteps = 100
N_store = 200
Nsub = 10
tlist = np.linspace(0, T, N_store)
psi0 = fock(N,0)
a = destroy(N)
def f1(t, args):
    return t/args["a"] 
def f2(t, args):
    return 1-t/args["a"]
sc_ops = [np.sqrt(gamma) * a, np.sqrt(gamma) * a*0.5]
h_t=[[a.dag() * a,f1],[a.dag() * a,f2]]
ssesolve(h_t, psi0, tlist, sc_ops, [],method='homodyne', args={"a":2})

