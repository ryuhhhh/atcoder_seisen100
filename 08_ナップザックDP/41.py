# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
# i日目に服を着るときi-1日目より前の服は関係ない
# なので、dp[i][j] = i日目に服jを選んだときの最大値
# として、i-1とiを比較しながらdp[i][j]を更新していく
D, N = map(int, input().split())

T = [int(input()) for _ in range(D)]
clothes = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i日目に服jを選んだときの最大値
dp = [[0] * N for _ in range(D)]

# 1日目
for i in range(N):
    if clothes[i][0] <= T[0] <= clothes[i][1]:
        dp[0][i] = clothes[i][2]

# 2日目以降(0-indexedなので1が2日目)
for i in range(1, D):
    # i日目に着る服
    for j in range(N):
        # 温度条件
        if clothes[j][0] <= T[i] <= clothes[j][1]:
            # i-1日目に着る服
            for k in range(N):
                # 1日目に入っている値は便宜上入れた初期値なので、
                # 2日目ではその値を加算をしない。
                # もし加算するとしたら-1日目が存在することになる。
                if i == 1:
                    dp[i][j] = abs(clothes[j][2] - clothes[k][2])
                # 3日目以降は前回の最大値を引き継ぐ
                if i >= 2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] +
                                   abs(clothes[j][2] - clothes[k][2]))

print(max(dp[-1]))
