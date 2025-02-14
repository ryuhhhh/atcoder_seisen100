# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
# bit全探索のカテゴリだがpythonは組み合わせを使用できるため簡潔に解ける

import itertools

N = 5
M = 3
A = [7, 4, 2, 6, 4]

C = [i for i in range(N)[1:]]

min_cost = 10000000000000000

# 最初の建物以外から残りを選択
for buiding_group in itertools.combinations(C, M-1):
    cost = 0
    last_height = A[0]
    # だんだんと大きくなるようにコストを追加
    for buiding in buiding_group:
        # 最後の建物の高さより小さい場合
        if A[buiding] <= last_height:
            cost += (last_height+1) - A[buiding]
            last_height += 1
        # 最後の建物の高さより大きい場合はそのまま
        else:
            last_height = A[buiding]
    min_cost = min(min_cost, cost)

print(min_cost)
