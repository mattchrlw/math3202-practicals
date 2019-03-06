# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from gurobipy import *

m = Model("Farmer Jones")

x1 = m.addVar(vtype=GRB.INTEGER) #chocolate
x2 = m.addVar(vtype=GRB.INTEGER) #plain

#Objective: maximuze total revenue

m.setObjective(4*x1 + 2*x2, GRB.MAXIMIZE)

m.addConstr(20*x1+ 50*x2<= 480)
m.addConstr(4*x1+ x2<= 30)
m.addConstr(0.25*x1 + 0.2*x2 <= 5)

m.optimize()

print("Bake", x1.x, "chocolate cakes")
print("Bake", x2.x, "plain cakes")
print("Revenue is ", m.objVal)