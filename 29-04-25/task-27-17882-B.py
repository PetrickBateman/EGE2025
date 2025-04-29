from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dis = 0
        for dot2 in cluster:
            sum_dis += dist(dot, dot2)
        distance.append([sum_dis, dot])
    return min(distance)[1]

with open('27_B_17882.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.split())
        if 0 < x < 4:
            cluster1.append([x, y])
        if 4 < x < 7:
            cluster2.append([x, y])
        else:
            cluster3.append([x, y])

center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x * 10000), int(ans_y * 10000))