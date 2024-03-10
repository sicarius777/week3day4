def capital_removal (orange):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    core = []
    for c in orange:
        if  c not in capitals:
            core.append(c)
    return "".join (core)

print(capital_removal("Roderick"))