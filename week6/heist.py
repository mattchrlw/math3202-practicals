#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:40:11 2019

@author: mattchrlw
"""

from gurobipy import *

S = range(16)
P = range(4)

SquaresUsed = [[(4,8,12,13),    (9,10,11,13),   (10,12,13,14),  
                (2,3,7,11),     (7,9,10,11)],
               [(2,6,9,10),     (4,8,9,10),     (2,3,6,10),     
                (0,1,2,6),      (0,1,4,8),      (8,9,10,14)],
               [(0,1,4,5),      (1,2,5,6),      (4,5,8,9),
                (5,6,9,10)],                                     
               [(12,13,14,15),  (3,7,11,15)]] 

Places = [range(len(SquaresUsed[p])) for p in P]

m = Model("Heist Puzzle")

X = {(p,i): m.addVar(vtype=GRB.BINARY) for p in P for i in Places[p]}

UseEachPiece = {p:
    m.addConstr(quicksum(X[p,i] for i in Places[p])==1)
    for p in P}

UseEachSquare = {s:
    m.addConstr(quicksum(X[p,i] for p in P for i in Places[p] 
        if s in SquaresUsed[p][i]) == 1)
    for s in S}

m.setParam('OutputFlag', 0)
    
while True:
    m.optimize()
    
    if m.status == GRB.INFEASIBLE:
        break
    
    for p in P:
        for i in Places[p]:
            if X[p,i].x > 0.99:
                print(p, SquaresUsed[p][i])
    m.addConstr(quicksum(X[k] for k in X if X[k].x >= 0.99) <= 3)
    print('---------------------')