# https://atcoder.jp/contests/abc145/tasks/abc145_c

import itertools
N = 8
X = [-406, 512, 494, -955, 128, -986, 763, 449]
Y = [10, 859, 362, -475, 553, -885, 77, 310]


def calc_dist(x1, y1, x2, y2):
    return ((x2-x1)*2+(y2-y1)**2)**0.5


dist_list = []
count = 0
# 各町の遷移の順列をループ
town = [i for i in range(N)]
for route in itertools.permutations(town):
    count += 1
    dist = 0
    # 1から始めるのは、最初の町からスタートするため
    for i in range(1, N):
        dist += calc_dist(X[route[i-1]], Y[route[i-1]],
                          X[route[i]], Y[route[i]])
    dist_list.append(dist)

print(sum(dist_list)/count)
