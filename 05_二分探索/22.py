# https://atcoder.jp/contests/arc054/tasks/arc054_b

# 今すぐにコンピュータを使用するか、少し待ってからコンピュータを使用するかのどちらが、
# 問題を解くのが早くなるのかを考える。
# 必要時間 = コンピュータを用意する時間 + そのコンピュータで解く時間
# f(x) = x + P/2^(x/1.5)
# 上記の1次関数の最小値を求める問題
# つまり微分して0となる点を求める問題

# 解法:
# f'(x)を5点近似で求める
# Pの値を入れた後に2分探索でf'(x)=0の値を求める

import bisect

P = 1000000000000000000.0000
EPS = 1e-8


def f(x):
    return x + P * 2 ** (-(x / 1.5))


def derivative_5_point(x, h=EPS):
    """
    5点近似で導関数を求める
    処理内容としては、中心差分を用いている
    """
    y1 = f(x + h)
    y2 = f(x - h)
    y3 = f(x + 2 * h)
    y4 = f(x - 2 * h)
    return (y4 - 8 * y2 + 8 * y1 - y3) / (12 * h)


def solve(left, right):
    # rightとleftは整数ではないため、
    # +1や-1を使用せずに、middleの更新を行う。
    while right-left > EPS:
        print(left, right)
        middle = (left+right)/2
        fc = derivative_5_point(middle)
        # 導関数が0に近いなら終了
        if abs(fc) < EPS:
            return middle
        # 左側の点の傾き と 中点の傾きが同じなら 関数はその範囲で減少しているため
        # 右側に解が存在する
        if derivative_5_point(left) * fc > 0:
            left = middle
        else:
            right = middle
    return (left+right)/2


if P < 2**(1.68/1.5):
    print(P)
    exit()
else:
    left = 0
    right = 1000
    print(f(solve(left, right)))
