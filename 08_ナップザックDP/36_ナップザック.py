N, W = map(int, input().split())
item = []
for i in range(N):
    item.append(list(map(int, input().split())))
print(item)

dp = [0 for _ in range(W+1)]

for i in range(0, N):
    for w in range(W+1):
        # これがないと入れ放題になってしまう。
        if item[i][1] <= w:
            dp[w] = max(dp[w], dp[w-item[i][1]]+item[i][0])
print(dp)
