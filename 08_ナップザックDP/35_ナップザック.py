N, W = map(int, input().split())
item = []
for i in range(N):
    item.append(list(map(int, input().split())))
print(item)

dp = [[0 for _ in range(W+1)] for i in range(N)]

for i in range(0, N):
    for w in range(W+1):
        if item[i][1] <= w:
            # 1つ前の同じ重さ か 1つ前の自身の重さを引いた値+自身の重さ
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-item[i][1]] + item[i][0])
        else:
            dp[i][w] = dp[i-1][w]
print(dp)
