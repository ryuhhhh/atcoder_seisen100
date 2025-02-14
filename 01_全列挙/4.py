# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c

N = 3  # 人数
M = 4  # 曲数
A = [[37, 29, 70, 41], [85, 69, 76, 50], [53, 10, 95, 100]]

sums = []
# 1つ目の曲を選ぶ
for i in range(M):
    # 2つ目の曲を選ぶ
    for j in range(i+1, M):
        sum = 0
        # 各人で2つの曲の中で大きい方を選ぶ
        for k in range(N):
            sum += max(A[k][i], A[k][j])
        sums.append(sum)
print(max(sums))
