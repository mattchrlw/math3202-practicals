from gurobipy import *

Arcs = [
    (0,2,100),
    (0,1,60), 
    (0,1,60),
    (1,2,100),
    (2,3,80), (2,3,80), 
    (3,5,20),
    (3,4,40), (3,4,40), (3,4,40), (3,4,40),
    (4,5,50), (4,5,50), (4,5,50), 
    (5,0,75), (5,0,75)
    ]

Names = ["Line 1", "Line 2", "Line 3", "Line 4",
        "Unload 1", "Unload 2",
        "StockPile Bypass",
        "Stacker 1", "Stacker 2", "Stacker 3", "Stacker4",
        "Reclaimer 1", "Reclaimer 2", "Reclaimer 3",
        "Load 1", "Load2"]

N = range(len(Names))
A = range(len(Arcs))
T = range(10)

m = Model("Coal Line Maintenance")

X = {(a,t): m.addVar() for a in A for t in T}
Y = {(a,t): m.addVar(vtype=GRB.BINARY) for a in A for t in T}

m.addConstrs(quicksum(Y[a,t] for a in A) <= 2 for t in T)
m.addConstrs(quicksum(Y[a,t] for t in T) == 1 for a in A)
m.addConstrs(quicksum(X[a,t] for a in A if Arcs[a][0] == n) == 
             quicksum(X[a,t] for a in A if Arcs[a][1] == n) 
             for n in N for t in T)
m.addConstrs(X[a,t] <= Arcs[a][2]*(1 - Y[a,t]) for a in A for t in T)
#m.addConstr((quicksum(X[a,t] for a in A if Arcs[a][0] == )))

m.setObjective(quicksum(X[14,t] + X[15,t] for t in T), GRB.MAXIMIZE)

m.optimize()

for a in A:
    for t in T:
        if Y[a,t].x > 0.99:
            print(Names[a], t)
            
for t in T:
    print(X[A[-1], t].x + X[A[-2], t].x, [Names[a] for a in A if Y[a,t].x > 0.99])
