for w in [0, 1]:
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                f = ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))
                if f:
                    print(x, y, z, w)
