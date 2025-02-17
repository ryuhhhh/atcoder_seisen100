# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# 無制限ナップザックDP
N, W = map(int, input().split())
item = []
for i in range(N):
    item.append(list(map(int, input().split())))

# 無制限だと1次元でいい
# 1回しか使えないときは 使う/使わない を管理するために2次元だった。
# それは縦軸をアイテム、横軸を重さにして、縦軸で入れるか入れないかを管理していた。
# 無制限のときは、その管理が不要であるため、1次元でいい。
# 各重さで自動で最大値を更新していく。
dp = [0 for _ in range(W+1)]

for i in range(0, N):
    for w in range(W+1):
        # これがないと入れ放題になってしまう。
        if item[i][1] <= w:
            dp[w] = max(dp[w], dp[w-item[i][1]]+item[i][0])
    print(dp)

print(dp[-1])
