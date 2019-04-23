def chess(t, s):
    if t == 2:
        if s < 0.99:
            return (0, "Lost")
        elif s > 1.01:
            return (1, "Won")
        else:
            return (0.45, "Bold")
    bold = (0.45 * chess(t + 1, s + 1)[0] + 0.55 * chess(t + 1, s)[0], "Bold")
    cons = (0.9 * chess(t + 1, s + 0.5)[0] + 0.1 * chess(t + 1, s)[0], "Cons")
    return max(bold, cons)


print((len(str(chess(0, 0))) + 4) * "—")
print("| " + str(chess(0, 0)) + " |")
print((len(str(chess(0, 0))) + 4) * "—")
