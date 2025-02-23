# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
# 横2列分だけ考えればよい
# つまりある列をRGBのどれかで塗ったら、次の列は前の列以外の色で塗り、その最小値を使えばいい。
N = int(input())
S = [input() for _ in range(5)]
color_list = "RBW#"
print(S)

# dp[i][j] = 左からi列目を色jで塗るときのコスト
# 縦軸は列、横軸は色
#   R B W
# 0
# 1
# 2
# 3
dp = [[0]*3 for _ in range(N+1)]

# 列
for i in range(1, N+1):
    # 色(黒は考えないため3まで)
    for j in range(3):
        cost = 0
        # 行
        for k in range(5):
            # 列iを1-indexedにしているため-1
            if S[k][i-1] != color_list[j]:
                cost += 1
        # ここがポイント
        # 今の列をjで塗るときのコストは、
        # 一つ前の列をj以外で塗るときのコストの最小値に今の列をjで塗るコストを足す
        colors = [0, 1, 2]
        colors.remove(j)
        dp[i][j] = min(dp[i-1][colors[0]], dp[i-1][colors[1]]) + cost

for row in dp:
    print(row)

print(min(dp[-1]))
