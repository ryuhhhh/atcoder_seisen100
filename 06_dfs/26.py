# https://atcoder.jp/contests/abc138/tasks/abc138_d
N = 4
G = [
    [1, 2],
    [2, 3],
    [2, 4]]

A = [
    [2, 10],
    [1, 100],
    [3, 1],]

# Gを隣接リストに変換
G2 = [[] for _ in range(N)]
score = [0 for _ in range(N)]
for g in G:
    G2[g[0]-1].append(g[1]-1)


def dfs(parent, value):
    score[parent] += value
    for child in G2[parent]:
        dfs(child, value)


# 加算する値と位置を渡す
for a in A:
    dfs(a[0]-1, a[1])


print(score)
