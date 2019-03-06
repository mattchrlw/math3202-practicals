#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:36:13 2019

@author: mattchrlw
"""

from gurobipy import *

cakes = ["Chocolate", "Plain"]
ingredients = ["Time", "Eggs", "Milk"]

C = range(len(cakes))
I = range(len(ingredients))

prices = [4,2]
available = [480,30,5]
usage = [
    [20,50],
    [4,1],
    [0.25,0.2]
]

m = Model("Farmer Jones")

X = {}
for c in C:
    X[c] = m.addVar(vtype=GRB.INTEGER)
    
m.setObjective(quicksum(prices[c]*X[c] for c in C), GRB.MAXIMIZE)

for i in I:
    m.addConstr(quicksum(usage[i][c]*X[c] for c in C) <= available[i])
    
m.optimize()

for c in C:
    print("Bake",X[c].x,cakes[c],"Cakes")