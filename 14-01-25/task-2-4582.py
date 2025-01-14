for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not(w <= z)) or (x <= y) or (not x)
                if not f:
                    print(w, x, y, z)