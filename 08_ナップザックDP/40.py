# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
# 参考: https://kakedashi-engineer.appspot.com/2020/06/09/joi2012yod/
MOD = 10**4
N, K = map(int, input().split())
A = {}
for _ in range(K):
    day, pasta = map(int, input().split())
    A[day-1] = pasta

# dp[d日目にいるとして][昨日のパスタpasta0][一昨日のパスタpasta1] のカウント
# たとえば1日目にいるとしたら、
# 0日目を考慮してN+1
dp = [[[0 for pasta1 in range(4)] for pasta0 in range(4)] for d in range(N+1)]

# 0日目について-1日目と-2日目はダミーなパスタとして0にしておく
# 0日目は [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]となるが、
# これは昨日がダミーパスタ(0番目の配列)で、一昨日がダミーパスタ(配列の0番目)であるカウントが1ということ
# 1日目は[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]となるが、
# これは昨日がパスタ1,2,3(1,2,3番目の配列)で、一昨日がダミーパスタ(配列の0番目)であるカウントが1ということ
# 2日目は[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]となるが、
# これは昨日がパスタ1,2,3(1,2,3番目の配列)で、一昨日がパスタ1,2,3(配列の1,2,3番目)であるカウントが1ということ
# 4,1,2日目を考えて9通りの組み合わせがあるということ
# これを繰り返していく
dp[0][0][0] = 1


# 日付
# 最初は0日目(day)と1日目(day+1)の間を考えることになる
for day in range(N):
    # 一昨日
    for pasta0 in range(4):
        # 昨日
        for pasta1 in range(4):
            # 今日
            # ダミーのパスタを消すために1からスタート
            # -1日目と-2日目にダミーのパスタがあったとしても、
            # これで0日目からは1からしかカウントしないので問題ない
            for pasta2 in range(1, 4):
                # パスタが指定されている場合はそれ以外をスキップ
                if day in A and A[day] != pasta2:
                    continue
                # 1,2日目と2,3日目の間で同じパスタが続かないならカウントを追加
                if pasta2 != pasta1 or pasta1 != pasta0:
                    dp[day+1][pasta2][pasta1] += dp[day][pasta1][pasta0]
                    dp[day+1][pasta2][pasta1] %= MOD

# 最終日、ダミーのパスタを除いて全ての状態の分を足す
ans = 0
for i in range(1, 4):
    for j in range(1, 4):
        ans += dp[-1][i][j]
        ans %= MOD

print(ans)
