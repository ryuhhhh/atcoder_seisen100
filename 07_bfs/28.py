# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
# BFSは,stack,visitedno2つで制御する。
n = 4
G = [
    [2, 4],
    [4],
    [],
    [3]
]
stack = [1]
result = [0] * n
cnt = 0
while stack:
    g = stack.pop(0)
    cnt += 1
    for next_g in G[g-1]:
        if result[next_g-1] == 0:
            result[next_g-1] = cnt
            stack.extend(G[next_g-1])
print(result)
