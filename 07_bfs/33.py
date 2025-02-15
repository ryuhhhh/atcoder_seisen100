# https://atcoder.jp/contests/abc088/tasks/abc088_d
# 答えは 全マス数 - 最短経路の長さ - 黒マスの数 = 不要な黒マスの数 となる
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

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while queue:
    row, column, cnt = queue.pop(0)
    if count[row][column] != -1:
        continue
    count[row][column] = cnt
    for d in directions:
        nrow = row + d[0]
        ncolumn = column + d[1]
        if 0 <= nrow < H and 0 <= ncolumn < W and M[nrow][ncolumn] != '#':
            queue.append([nrow, ncolumn, cnt+1])

print(H*W - count[H-1][W-1] - blacks)
