# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
"""
問題から中央値が答えだという法則が見つかる
"""
import statistics
N = 5
A = [1, 43, 13, 14, 79]
B = [71, 64, 35, 54, 85]

IN_MEDIAN = statistics.median(A)
OUT_MEDIAN = statistics.median(B)

sum = 0
for i in range(N):
    # 入口からAまでの距離
    sum += abs(A[i] - IN_MEDIAN)
    # AからBまでの距離
    sum += B[i] - A[i]
    # Bから出口までの距離
    sum += abs(OUT_MEDIAN - B[i])
print(sum)
