# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
# n = int(input())
# m = int(input())
# A = [list(map(int, input().split())) for l in range(m)]

A = [
    [1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
]


def dfs(row, column, cnt):
    global ans
    # すでに割られていたら終了
    if A[row][column] == 0:
        return
    ans = max(cnt, ans)
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dx, dy in d:
        nrow = row + dy
        ncolumn = column + dx
        if 0 <= nrow < len(A) and 0 <= ncolumn < len(A[0]):
            # 今のマスを割って
            A[row][column] = 0
            # 次のマスに移動
            dfs(nrow, ncolumn, cnt+1)
            # 移動しきったら戻りながら元に戻す
            A[row][column] = 1


ans = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        # 各マスをスタート地点としてdfs
        # 各dfsが終わったタイミングでマスを元に戻す
        dfs(i, j, 1)
print(ans)
