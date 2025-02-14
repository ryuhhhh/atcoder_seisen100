# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
A = [
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0]]

visited = [[False for _ in range(len(A[0]))] for _ in range(len(A))]


def dfs(x, y):
    if visited[y][x]:
        return
    visited[y][x] = True
    if x-1 >= 0 and A[y][x-1]:
        dfs(x-1, y)
    if x+1 < len(A[0]) and A[y][x+1]:
        dfs(x+1, y)
    if y-1 >= 0 and A[y-1][x]:
        dfs(x, y-1)
    if y+1 < len(A) and A[y+1][x]:
        dfs(x, y+1)
    # 斜め
    if x-1 >= 0 and y-1 >= 0 and A[y-1][x-1]:
        dfs(x-1, y-1)
    if x-1 >= 0 and y+1 < len(A) and A[y+1][x-1]:
        dfs(x-1, y+1)
    if x+1 < len(A[0]) and y-1 >= 0 and A[y-1][x+1]:
        dfs(x+1, y-1)
    if x+1 < len(A[0]) and y+1 < len(A) and A[y+1][x+1]:
        dfs(x+1, y+1)


cnt = 0
for y in range(len(A)):
    for x in range(len(A[0])):
        if A[y][x] and not visited[y][x]:
            dfs(x, y)
            cnt += 1

print(cnt)
