# v_t(s) = \min_{0 \leq a \leq s} ( (1-p_{ta}) \cdot v_{t+1}(s-a) )

data = [
    [0.20, 0.30, 0.35, 0.38, 0.40],  # Algebra
    [0.25, 0.30, 0.33, 0.35, 0.38],  # Calculus
    [0.10, 0.30, 0.40, 0.45, 0.50],  # Statistics
]


def value(t, s):
    if t >= 3:
        return (1, 0)
    return min(((1 - data[t][a]) * value(t + 1, s - a)[0], a) for a in range(s + 1))


for i in range(5):
    for j in range(5):
        print("(", i, ",", j, "): ", value(i, j), sep="")
