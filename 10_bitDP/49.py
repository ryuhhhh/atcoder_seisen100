# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja

V, E = map(int, input().split())

distances = [[float('inf')]*V for _ in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    distances[s][t] = d

# dp[通った都市][今いる都市] = 最短距離
# 1 << V は 2^V 通りの都市の組み合わせ
# たとえば1 << 4 なら 0000, 0001 ... 1111の16通りのループ
dp = [[float("inf")] * V for _ in range(1 << V)]
# ある都市から出発すればいいので0からスタートしても問題ない
dp[0][0] = 0

# 通った都市
for s in range(1 << V):
    # 今いる都市
    for i in range(V):
        # 通ったことがない都市はスキップ
        # s=0000なのに、i=1のときはスキップ
        # 一方でs=0000で、i=0なら通った都市は0で今いる都市は0ということになる
        if dp[s][i] == float("inf"):
            continue
        # 都市iから都市jに移動
        for j in range(V):
            # すでに通った都市はスキップ
            # 例えばs = 0001でj=2のときはスキップしない
            # 例えばs = 0010でj=2のときはスキップ
            if s >> j & 1:
                continue
            # 次の都市の今の値と、今の都市の値+移動距離を比較して小さい方を採用
            # 例えばs=0000, i=0, j=1のとき、
            # dp[0001][1] = min(dp[0001][1], dp[0000][0] + distances[0][1])
            # 0001は都市1に行ったことがあるという意味
            dp[s + (1 << j)][j] = min(dp[s + (1 << j)][j],
                                      dp[s][i] + distances[i][j])

for i, row in enumerate(dp):
    print(f"{i:04b}", row)

print(dp[(1 << V)-1][0])
