# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
import bisect

# 環状線の長さ
d = 20
# 店舗の数
N = 4
# 注文の数
M = 4
# [0]と[d]は本店
D = [0] + [12, 8, 16] + [d]
D = sorted(D)
# 注文の位置
K = [7, 7, 11, 8]
sum = 0
for i in range(len(K)):
    # bisect_leftは挿入位置を返す
    # _leftと_rightの違いは、同じ値がある場合にその左右どちらに挿入するか
    pos = bisect.bisect_left(D, K[i])
    sum += D[pos]-K[i]
print(sum)
