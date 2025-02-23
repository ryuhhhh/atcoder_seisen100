# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp

# 問題文より10^6以下の正四面体数を求める
cnt = 1
value = 0
nums = []
nums_kisu = []
while value < 10**6:
    value = cnt * (cnt + 1) * (cnt + 2) // 6
    cnt += 1
    nums.append(value)
    if value % 2 == 1:
        nums_kisu.append(value)


while True:
    n = int(input())
    if n == 0:
        break
    # dp[i]: iを作るのに必要な最小の正四面体数の個数
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    # その値
    for i in range(1, n + 1):
        # 正四面体
        for j in range(len(nums)):
            if nums[j] <= i:
                # その値を作るのに必要な最小の正四面体数の個数は、
                # その値 or その値 - nums[j]を作るのに必要な最小の正四面体数の個数 + 1
                dp[i] = min(dp[i], dp[i - nums[j]] + 1)

    # 奇数だけを使って作るだけ
    dp_kisu = [float("inf")] * (n + 1)
    dp_kisu[0] = 0
    for i in range(1, n + 1):
        for j in range(len(nums_kisu)):
            if nums_kisu[j] <= i:
                dp_kisu[i] = min(dp_kisu[i], dp_kisu[i - nums_kisu[j]] + 1)
    print(dp[-1], dp_kisu[-1])
