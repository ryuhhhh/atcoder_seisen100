# https://atcoder.jp/contests/abc002/tasks/abc002_4
# M (0≦M≦N(N−1)/2)の範囲は、
# 1人目は残りのN−1人との関係を考える、2人目は残りのN−2人との関係を考える、というように考えると、
# 階差数列の和の公式を使って、Mの範囲はN(N−1)/2までとなる。
# N=3なら1人目は2人との関係を、2人目は1人との関係を考えるので、Mの範囲は3まで。

import itertools
N = 7
M = 9

link = [
    (7, 9),
    (1, 2),
    (1, 3),
    (2, 3),
    (4, 5),
    (4, 6),
    (4, 7),
    (5, 6),
    (5, 7),
    (6, 7)]

ans = 0
# 議員の組み合わせをbitで表現しループ
# reversedとするのは、最大の組み合わせから調べるため
# つまりbit=1111111, 1111110, 1111101, 1111100, ... 0000000
for bit in reversed(range(1 << N)):
    group = []
    # bitの各桁で1が立っている議員をgroupに追加
    for i in range(N):
        if bit >> i & 1:
            group.append(i+1)
    exist = True
    # group内の議員2人の組み合わせがlinkに含まれているか確認
    # itertools.combinations(group, 2)でgroup内の2人の組み合わせを作成
    for j in itertools.combinations(group, 2):
        if j not in link:
            exist = False
            break
    # 最大順にループしているため、最初に見つかったgroupが最大のgroup
    if exist:
        break

print(len(group) if len(group) else 1)
