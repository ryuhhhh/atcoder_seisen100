# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
# 煎餅を裏返す直前にいくつかのせんべいが裏返ったので、素早く表になるべく戻そう。
# つまりなるべく1(裏)から0(表)に戻すことが目標。
# R の上限 10 は C の上限 10000 に比べて小さいので、行を先にひっくり返すことを考える

N = 3
M = 6
A = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1]
]

# 行数 <= 10,列数 <= 10000
# answer is 15


# ある行をひっくり返す
def reverse_row(S, pos):
    for i in range(M):
        # ^= 1 はxor演算で11なら0,01なら1に変換する
        S[pos][i] ^= 1


# ある列の表(0)または裏(1)の多いほうを持ってくる
# 表ならそのままカウントできるし、
# 裏ならひっくり返せば表になるのでカウントできる。
def get_0_or_1_max_count(S, pos):
    count1 = 0
    for i in range(N):
        count1 += S[i][pos]
    count0 = N - count1
    return max(count1, count0)


result = 0
# 裏返す行をbit全探索
# i=000,001,010,011,100,101,110,111
for i in range(1 << N):
    S = A
    # j でループしてひっくり返す行を決める
    for j in range(N):
        # &1 で最下位ビットが1かどうかを判定する
        # つまり101なら、1行目と3行目をひっくり返す
        if i >> j & 1:
            reverse_row(S, j)
    sum = 0
    for k in range(M):
        sum += get_0_or_1_max_count(S, k)

    result = max(result, sum)

print(result)

# 行からループした場合の計算量は、
# 2^3 * 3(行分のbit探索) * 6(列分のxor) = 144 となり、
# 反対に列から先にループすると
# 2^6 * 6(列分のbit探索) * 3(行分のxor) = 432 となり、行から先にループするよりも多くなる
