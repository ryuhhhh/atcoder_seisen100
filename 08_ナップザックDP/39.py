# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
# 1つ目が8なら8のカウントが+1
# 2つ目が3なら 8+3=11, 8-3=5 のカウントが+1
# 3つ目が2なら 11+2=13, 11-2=9, 5+2=7, 5-2=3 のカウントが+1
# つまりdp[i][j] = i個目までの数字を使い、数字jを作ることができるカウントとして、
# i=3,j=13 なら i-1=2,j=11 のカウントが1なら、dp[3][13] += dp[2][13-2=11] = 1 となる
#  ...のようにdpを作ればよい
N = int(input())
items = [int(i) for i in input().split()]
value = items[-1]
items = items[:-1]

# i個目までの数字を使い、数字jを作ることができるカウントを入れる
dp = [[0 for j in range(20+1)] for i in range(N-1)]
# 最初の数字以外は全て0
# なので問題のように最初の数字が8なら dp[0][8] = 1
dp[0][items[0]] = 1

for i in range(1, N-1):
    for j in range(20+1):
        # jを作れるということは、1つ前の数字を使って作れる、j-items[i]かj+items[i]のカウントをもらえる
        if j + items[i] <= 20:
            # i=1で、8 3 2...なら
            # dp[1][0] += dp[0][0+3]
            # dp[1][1] += dp[0][1+3]
            # dp[1][2] += dp[0][2+3]
            # ...
            # dp[1][5] += dp[0][5+3]
            # つまり1番目の数字-2番目の数字で5を作れる(8-3=5=j)
            dp[i][j] += dp[i-1][j+items[i]]
        if 0 <= j - items[i]:
            # 同じく1番目の数字+2番目の数字で11を作れる(8+3=11=j)
            dp[i][j] += dp[i-1][j-items[i]]

for i in dp:
    print(i)
print(dp[-1][value])
