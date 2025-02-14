n, m = map(int, input().split())
C = list(map(int, input().split()))

dp = [100 for _ in range(n+1)]
dp[0] = 0
for i in range(m):
    for j in range(n+1):
        # これがないとマイナスのインデックスとなる
        if j >= C[i]:
            # 金額が大きくなればスキップする長さが長くなるイメージ
            dp[j] = min(dp[j], dp[j-C[i]]+1)
print(dp)
