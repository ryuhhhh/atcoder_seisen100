# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
# DixCjの疲労がたまる
# その日に移動するか否かを動的計画法で全列挙

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

# dp[i][j]: 都市iでj日目にいる際の疲労感の最小値
dp = [[float('inf')] * (M+1) for _ in range(N+1)]

# 都市0での各日付での疲労感は0
# 縦軸は都市、横軸は日付
#     0   1   2   3   4   5　
# 0   0   0   0   0   0   0
# 1 inf inf inf inf inf inf
# 2 inf inf inf inf inf inf
# 3 inf inf inf inf inf inf
for i in range(M+1):
    dp[0][i] = 0

# 都市
for i in range(1, N+1):
    # 日付
    for j in range(1, M+1):
        # 貰うDP
        # 昨日の1つ前の地点から移動 or 昨日の地点でそのまま今日を過ごす
        # i-1とj-1を使うことで右下への移動か、
        # またはiとj-1を使うことで右への移動が可能
        dp[i][j] = min(dp[i-1][j-1] + D[i-1]*C[j-1], dp[i][j-1])

for row in dp:
    print(row)
