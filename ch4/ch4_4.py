# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 01:52:10 2021

@author: Aerial
"""
# Import lib
import numpy as np
import sympy as sp
from sympy import * 
import matplotlib.pyplot as plt

# u = U_nod * (1+x/L)
# v = -1 * U_nod * (y/L)
# Solve for dydx = v/u
x, y, U_nod, L = sp.symbols("x, y, U_nod, L")
# Left hand side of the eq
lhs = 1 / (U_nod * (1 + x/L))
# Integrate left hand side of the eq
lhs_int = sp.integrate(lhs,x)
sp.simplify(lhs_int)
print("Left handside of ODE equals = {0}".format(lhs_int))
# Right hand side of the eq
rhs = 1 / (U_nod * (y / L))
# Integrate right hand side of the eq
rhs_int = sp.integrate(rhs,y)
sp.simplify(rhs_int)
print("Right handside of ODE equals = {0}".format(rhs_int))
# Set rhs_int = lhs_int ( seperable ODE ) 
# After solving for y, we plot for 4 different values of constant

# Define variables 
C1 = 1.0
C2 = 0.75
C3 = 0.50
C4 = 0.25
L = 1.0 
# Set L = 1 so we can plot for x/L and y/L 
x = np.linspace(0,2,150)
y1 = L*C1 / (1 + x / L)
y2 = L*C2 / (1 + x / L)
y3 = L*C3 / (1 + x / L)
y4 = L*C4 / (1 + x / L)

# Plot
plt.figure()
plt.xlabel("[ x/L ]")
plt.ylabel("[ y/L ]")
plt.plot(x,y1 ,color='red', label = "C = 1.00")
plt.plot(x,y2 ,color='grey', label = "C = 0.75")
plt.plot(x,y3 ,color='black', label = "C = 0.50")
plt.plot(x,y4 ,color='blue', label = "C = 0.25")
plt.legend()
plt.savefig("ch4_4.pdf", dpi = 300)