#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:05:16 2019

@author: mattchrlw
"""

from gurobipy import *

# Data
Products = {
        'German Cars':          [10.3, 'Car',       'Germany'],
        'Japanese Cars':        [10.1, 'Car',       'Japan'],
        'American Computers':   [11.8, 'Computer',  'USA'],
        'Singaporean Computers':[11.4, 'Computer',  'Singapore'],
        'European Appliances':  [12.7, 'Appliance', ''],
        'Asian Appliances':     [12.2, 'Appliance', ''],
        'German Insurance':     [9.5,  'Insurance', 'Germany'],
        'American Insurance':   [9.9,  'Insurance', 'USA'],
        'Short-term Bonds':     [3.6,  'Bonds',     ''],
        'Medium-term Bonds':    [4.2,  'Bonds',     '']
}

# Index 0 represents minimum value, index 1 represents maximum value
Options = {
        'Car':          [0,     30000],
        'Computer':     [0,     30000],
        'Appliance':    [0,     20000],
        'Insurance':    [20000, GRB.INFINITY],
        'Bonds':        [25000, GRB.INFINITY]
}

Countries = {
        'Germany':  [0,50000],
        'Japan':    [0,40000],
        'USA':      [0,GRB.INFINITY],
        'Singapore':[0,GRB.INFINITY]
}

Available = 100000

# Create model
m = Model("Portfolio Optimisation")

# Add variables
X = {p: m.addVar() for p in Products}

# Set objective function
m.setObjective(quicksum(Products[p][0]*X[p] for p in Products), GRB.MAXIMIZE)

# Add constraints
for o in Options:
    m.addConstr(quicksum([X[p] for p in Products if Products[p][1] == o]) >= Options[o][0])
    m.addConstr(quicksum([X[p] for p in Products if Products[p][1] == o]) <= Options[o][1])

for c in Countries:
    m.addConstr(quicksum([X[p] for p in Products if Products[p][2] == c]) >= Countries[c][0])
    m.addConstr(quicksum([X[p] for p in Products if Products[p][2] == c]) <= Countries[c][1])


m.addConstr(X['Short-term Bonds'] >= 0.4*X['Medium-term Bonds'])
m.addConstr(quicksum([X[p] for p in Products]) <= Available)

m.optimize()

if m.status == GRB.OPTIMAL:
    for p in Products:
        print(p, X[p].x)
print('Total return = $', m.objVal)

Constraints = m.getConstrs()

for c in Constraints:
    print(c.ConstrName, c.RHS, c.Slack, c.Pi, c.SARHSLow, c.SARHSUp)
    
for p in Products:
    print(p, X[p].x, X[p].RC)