# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp
# 入力信号とコードブックが入力
# 128から始まる数列を作成し元の入力信号の二乗差分の和が最小になるような数列を求める
# y0 = 128
# yn = yn-1 + C[kn]
# C = {コードブックの値}

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    C = []
    for _ in range(M):
        C.append(int(input()))
    X = []
    for _ in range(N):
        X.append(int(input()))

    # dp[i][j] = i番目までの入力信号を処理し、最後の値がjであるときの最小二乗差分の和
    dp = [[float('inf') for _ in range(256)] for _ in range(N+1)]
    # 何も数字を使用していない場合は128が0
    #             0   1   2 ... 128 ... 255
    #  x0(none) inf inf inf ...   0 ... inf
    #  x1       inf inf inf ... inf ... inf <-- ここからスタート
    #  x2       inf inf inf ... inf ... inf
    # 128だけを0にすることで、最初の値が128であることを表現
    # なぜならinfとinf+差分だとinfになるため
    dp[0][128] = 0

    # 数字
    for i in range(1, N+1):
        # 数列の値
        for j in range(256):
            # コードブックの値=dpを遷移する際に使用する値
            for c in C:
                to = j + c
                if to < 0:
                    to = 0
                elif to > 255:
                    to = 255
                # 現在のtoの値 or 1つ前のto-コードブックの値に差分を加えた値
                dp[i][to] = min(dp[i][to], dp[i-1][j] + (X[i-1] - to) ** 2)
    print(min(dp[N]))
