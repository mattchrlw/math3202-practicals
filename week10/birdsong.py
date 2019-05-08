B = {
    -6.4: 0.25,
    0: 0.50,
    6.4: 0.25
}

E = 32
D = 3.6

# Memoize gang
_V = {}

def x(i,E,D):
    return (i + E - D)

def p(x):
    return x - int(x)

def singing(i,b):
    return 12 + 0.002*i + b

def foraging(i,b):
    return 8 + 0.007*i + b

def V(t,i,m):
    if i <= 0:
        return (0, 'Starved')
    if t == 150:
        if m == 1:
            return (2, 'Mate')
        else:
            return (1, 'Alive')
    if t >= 65:
        return (V(t+1, x(i, 0, 3.6), m), 'Rest')

    if (t,i,m) not in _V:
        _V[t,i,m] = max(
            # Rest
            V(t+1, x(i, 0, 3.6), m),
            # Forage
            0.6*(sum(B[b]*(V(t+1, x(i, 32, foraging(i, b)), m)) for b in B))
            + (1 - 0.6)*(sum(B[b]*(V(t+1, x(i, 0, foraging(i, b)), m)) for b in B)),
            # Singing
            0.004*(sum(B[b]*(V(t+1, x(i, 0, singing(i, b)), 1)) for b in B)) 
            + (1-0.004)*(sum(B[b]*(V(t+1, x(i, 0, singing(i, b)), m)) for b in B))
        )
    
    return _V[t,i,m]

print(V(150, 1, 0))
print(V(150, 1, 1))
print(V(149, 1, 1))
