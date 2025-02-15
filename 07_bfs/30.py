# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
# 1~Nまでのチーズで、すべての固さは異なり、
# 1つずつ食べていくので、結局食べる順番は決まっている
H, W, N = map(int, input().split())
M = []
cheese = {}
# マップの作成
for i in range(H):
    s = input()
    inner_M = []
    # 1行ずつ見ていく
    for j in range(W):
        # スタート地点を記録
        if s[j] == "S":
            start = [i, j]
        # チーズの位置を記録
        if s[j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            cheese[int(s[j])] = [i, j]
        # マス目を数字に変換
        if s[j] in ["S", "."]:
            inner_M.append(10)
        elif s[j] in ["X"]:
            inner_M.append(11)
        else:
            inner_M.append(int(s[j]))
    M.append(inner_M)

# チーズから次のチーズまでの距離をカウントしていく
# 3次元配列で、[row, column, 移動距離, 体力]をスタックに入れていく
queue = [[start[0], start[1], 0, 1]]
# N個のチーズを食べる
for _ in range(N):
    # 次のチーズを探す旅に毎回初期化
    visited = [[False for _ in range(W)] for _ in range(H)]
    while queue:
        row, column, dist, life = queue.pop(0)
        # 自分の体力と同じ固さのチーズ発見
        if [row, column] == cheese[life]:
            life += 1
            if life == N+1:
                print(dist)
                exit()
            # queueを初期化して次のチーズを探す
            queue = [[row, column, dist, life]]
            break
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dx, dy in d:
            nrow = row + dy
            ncolumn = column + dx
            # 11は障害物
            if 0 <= nrow < H and 0 <= ncolumn < W and\
                    not visited[nrow][ncolumn] and M[nrow][ncolumn] != 11:
                visited[nrow][ncolumn] = True
                queue.append([nrow, ncolumn, dist+1, life])
