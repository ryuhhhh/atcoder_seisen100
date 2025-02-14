# https://atcoder.jp/contests/abc077/tasks/arc084_a
import bisect
N = 6
A = [3, 14, 159, 2, 6, 53]
B = [58, 9, 79, 323, 84, 6]
C = [2643, 383, 2, 79, 50, 288]

A = sorted(A)
C = sorted(C)

# N = 3
# A = [1, 1, 1]
# B = [2, 2, 2]
# C = [3, 3, 3]

sum = 0
for i in range(N):
    # Bより真に小さいAの個数を求めるために位置を取得
    pos_a = bisect.bisect_left(A, B[i])
    # Bより真に大きいCの個数を求めるために位置を取得
    pos_c = bisect.bisect_right(C, B[i])
    sum += pos_a * (N - pos_c)
print(sum)
