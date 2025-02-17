# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i]: i円支払うのに必要な最小のコインの「枚数」
# 無制限ナップザックなので1次元DP
dp = [100 for _ in range(n+1)]
# 0円支払うのに必要なコインの枚数は0枚
dp[0] = 0
# m種類のコインを縦軸
for i in range(m):
    # n円の支払いを横軸
    for j in range(1, n+1):
        # 各支払い上限は超えない
        # j-coins[i] で比較することができなくなるため
        if j < coins[i]:
            continue
        dp[j] = min(dp[j], dp[j-coins[i]]+1)
print(dp[-1])
