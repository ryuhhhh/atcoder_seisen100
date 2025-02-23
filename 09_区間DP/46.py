n = int(input().strip())
dimensions = []

for _ in range(n):
    r, c = map(int, input().split())
    # 連鎖行列なのでrは最初の値だけでいい
    if not dimensions:
        dimensions.append(r)
    dimensions.append(c)

# dp[left][right]: leftからrightまでの行列を掛けるときの最小コスト
dp = [[0] * n for _ in range(n)]

# 長さlengthの部分問題を解く
for length in range(2, n + 1):
    for left in range(n - length + 1):
        # 最初はlength=2,left=0,right=1
        # 次はlength=2,left=1,right=2
        # つまりlength=2でleftをずらしていく
        # lengthはleftを含めての長さなので-1をする
        right = left + length - 1
        dp[left][right] = float("inf")
        for k in range(left, right):
            # 最初は長さが2なので、隣り合う行列の積のコストがそのまま入る
            # それ以降は、kを境に左右に分けて考える
            # たとえばleft=0,right=2のとき、
            # k=0のときは0-0,1-2に分けて、
            # k=1のときは0-1,2-2に分ける
            # そうすることで0-1-2の最小コストを求めることができる
            cost = dp[left][k] + dp[k + 1][right] +\
                dimensions[left] * dimensions[k + 1] * dimensions[right + 1]
            dp[left][right] = min(dp[left][right], cost)

for row in dp:
    print(row)

print(dp[0][n - 1])
