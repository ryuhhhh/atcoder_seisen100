# https://www2.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho.pdf#page=6
# 半分全列挙 + 二分探索
# 4個選択を2個選択と2個選択に分ける
# 2個選択(投げないを含む)で可能な値を全列挙 -> S
# Sから1つ選ぶ -> S1
# M-S1の値が残りなので これを超えない範囲で二分探索でSの中の最大の値をとる -> S2
# S1 + S2 が答え
# 半分全列挙をせず全探索する場合はO(N^4)
# 半分全列挙をすることでO(N^2*logN(二分探索))になる

import bisect

N = 4
M = 50
A = [3, 14, 15, 9] + [0]  # 0は選択しないということ

# 半分全列挙
S = set()
for i in range(len(A)):
    for j in range(len(A)):
        S.add(A[i]+A[j])
S = list(S)
S.sort()
print(S)

max_score = 0
for s1 in S:
    remain = M - s1
    # 挿入する直前が残り獲得できる最大値
    s2_index = bisect.bisect_left(S, remain) - 1
    max_score = max(max_score, s1+S[s2_index])
print(max_score)
