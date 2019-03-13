from gurobipy import *

Oils = ['Veg 1', 'Veg 2', 'Oil 1', 'Oil 2', 'Oil 3']
OilType = [0,0,1,1,1]
Months = ['January', 'February', 'March', 'April', 'May', 'June']

Cost = [[110,130,110,120,100,90],
        [120,130,140,110,120,100],
        [130,110,130,120,150,140],
        [110,90,100,120,110,80],
        [115,115,95,125,105,135]]
Hardness = [8.8, 6.1, 2.0, 4.2, 5.0]
MinHardness = 3
MaxHardness = 6
Max = [200, 250]
StoreCost = 5
StoreMax = 1000
Initial = [500,500,500,500,500]
SellPrice = 150

m = Model("Oil Blending 2")

O = range(len(Oils))
T = range(len(Months))

X = {}
Y = {}
S = {}
for o in O:
    for t in T:
        X[o,t] = m.addVar()
        Y[o,t] = m.addVar()
        S[o,t] = m.addVar()
        
m.setObjective(quicksum(SellPrice*X[o,t] for o in O for t in T)
             - quicksum(Cost[o][t]*Y[o,t] for o in O for t in T)
             - quicksum(StoreCost*S[o,t] for o in O for t in T), GRB.MAXIMIZE)

for t in T:
    m.addConstr(quicksum(X[o,t] for o in O if OilType[o] == 0) <= Max[0])
    m.addConstr(quicksum(X[o,t] for o in O if OilType[o] == 1) <= Max[1])
    m.addConstr(quicksum(Hardness[o] - MinHardness for o in O)*X[o,t] >= 0)
    m.addConstr(quicksum(Hardness[o] - MaxHardness for o in O)*X[o,t] <= 0)
    for o in O:
        m.addConstr(S[o,t] <= StoreMax)
        if t == 0:
            m.addConstr(S[o,t] == Initial[o] - X[o,t] + Y[o,t])
        else:
            m.addConstr(S[o,t] == S[o,t-1] - X[o,t] + Y[o,t])
            
m.optimize()

for t in T:
    print([X[o,t].x for o in O])
    print([Y[o,t].x for o in O])
    print([S[o,t].x for o in O])