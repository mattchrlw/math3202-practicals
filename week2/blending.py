from gurobipy import *

Oils = ['Veg 1', 'Veg 2', 'Oil 1', 'Oil 2', 'Oil 3']
OilType = [0,0,1,1,1]

Cost = [110, 120, 130, 110, 115]
Hardness = [8.8, 6.1, 2.0, 4.2, 5.0]
MinHardness = 3
MaxHardness = 6
Max = [200, 250]

SalePrice = 150

O = range(len(Oils))

m = Model("Blending Problem")

X = {}
for o in O:
    X[o] = m.addVar()
    
m.setObjective(SalePrice*quicksum(X[o] for o in O)-quicksum(Cost[o]*X[o] for o in O), GRB.MAXIMIZE)

Quantity = [0,0]

for o in O:
    m.addConstr(X[o] >= 0)
    m.addConstr(quicksum(X[o]*Hardness[o] for o in O) <= MaxHardness*quicksum(X[o] for o in O))
    m.addConstr(quicksum(X[o]*Hardness[o] for o in O) >= MinHardness*quicksum(X[o] for o in O))
    Quantity[OilType[o]] += X[o]
        
for i in [0,1]:
    m.addConstr(Quantity[i] <= Max[i])

m.optimize()

for o in O:
    print("Produce", X[o].x, "tons of", Oils[o])

print("Profit:", m.objVal)