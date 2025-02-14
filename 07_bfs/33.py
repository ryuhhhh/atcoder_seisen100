# https://atcoder.jp/contests/abc088/tasks/abc088_d
H, W = map(int, input().split())
M = []
blacks = 0
for i in range(H):
    inner_M = []
    row = input()
    for j in range(W):
        inner_M.append(row[j])
        if row[j] == "#":
            blacks += 1
    M.append(inner_M)

count = [[-1 for _ in range(W)] for _ in range(H)]

queue = [[0, 0, 1]]
# result = [0 for _ in range(H*W)]

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while queue:
    y, x, cnt = queue.pop(0)
    if count[y][x] != -1:
        continue
    count[y][x] = cnt
    # result[cnt] += 1
    for d in directions:
        ny = y + d[0]
        nx = x + d[1]
        if 0 <= ny < H and 0 <= nx < W and M[ny][nx] != '#':
            queue.append([ny, nx, cnt+1])

print(H*W - count[H-1][W-1] - blacks)
