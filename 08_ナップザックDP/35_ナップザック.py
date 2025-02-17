# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja
# ナップザックDPは、逐一各容量での最大値を更新していく問題。
N, W = map(int, input().split())
item = []
for i in range(N):
    item.append(list(map(int, input().split())))
print(item)

# dpは、縦軸は品物の個数、横軸は重さ
dp = [[0 for _ in range(W+1)] for i in range(N)]

for item_index in range(0, N):
    # 重さが0からWまで
    for w in range(W+1):
        # 荷物が入るなら
        if item[item_index][1] <= w:
            # 1つ前の同じ重さ か 1つ前の自身の重さを引いた値+自身の重さ
            dp[item_index][w] = max(
                dp[item_index-1][w], dp[item_index-1][w-item[item_index][1]]+item[item_index][0])
        # 入らないなら前回の同じ容量の値を引き継ぐ
        else:
            dp[item_index][w] = dp[item_index-1][w]
print(dp[-1][-1])
