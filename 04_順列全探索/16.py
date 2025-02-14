# https://atcoder.jp/contests/abc150/tasks/abc150_c
# ans 17517

import itertools
N = 8
A = (7, 3, 5, 4, 2, 1, 6, 8)
B = (3, 8, 2, 5, 4, 6, 7, 1)
C = [i+1 for i in range(N)]

count1 = 0
if1 = True
count2 = 0
if2 = True

# permutationsは順列を生成する関数で、その順番は辞書順
for p in itertools.permutations(C):
    if if1:
        count1 += 1
    if if2:
        count2 += 1
    # 一致する数字が見つかったら、その順列のカウンターはストップ
    if p == A:
        if1 = False
    if p == B:
        if2 = False
    # どちらも見つかったら終了
    if not if1 and not if2:
        break
print(abs(count1-count2))
