# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
N = int(input())
items = [int(i) for i in input().split()]
value = items[-1]
items = items[:-1]

# i個目の数字を使い、j番目の数字を作ることができるカウントを入れる
dp = [[0 for j in range(20+1)] for i in range(N-1)]
# 最初の数字以外は全て0
dp[0][items[0]] = 1

for i in range(1, N-1):
    for j in range(20+1):
        if j + items[i] <= 20:
            dp[i][j] += dp[i-1][j+items[i]]
        if 0 <= j - items[i]:
            dp[i][j] += dp[i-1][j-items[i]]

print(dp[-1][value])
