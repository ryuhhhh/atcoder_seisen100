# https://atcoder.jp/contests/abc007/tasks/abc007_3
R, C = map(int, input().split())
S = [int(i) for i in input().split()]
G = [int(i) for i in input().split()]
M = [[a for a in input()] for _ in range(R)]

result = [[0 for _ in range(C)] for _ in range(R)]
# stackに位置とカウントを入れると便利
stack = [[S[0]-1, S[1]-1, 0]]
result[S[0]-1][S[1]-1] = 0
cnt = 1
while stack:
    row, column, cnt = stack.pop(0)
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dx, dy in d:
        nrow = row + dy
        ncolumn = column + dx
        if 0 <= nrow < R and 0 <= ncolumn < C and M[nrow][ncolumn] == "."\
                and result[nrow][ncolumn] == 0:
            result[nrow][ncolumn] = cnt + 1
            stack.append([nrow, ncolumn, cnt+1])
print(result[G[0]-1][G[1]-1])
