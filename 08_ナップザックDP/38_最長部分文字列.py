# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
n = int(input())
S = []
for i in range(n):
    str_set = []
    for j in range(2):
        str_set.append(input())
    S.append(str_set)


for str_set in S:
    # 縦軸と横軸の長さはそれぞれの文字列の長さ+1
    # 0を置くのは1行目や1列目でmaxを取るときにエラーが出るのを防ぐため
    dp = [[0 for _ in range(len(str_set[1])+1)]
          for _ in range(len(str_set[0])+1)]
    # 0番目は何も選択しないを表すためスキップ
    for i in range(1, len(str_set[0])+1):
        # 0番目は何も選択しないを表すためスキップ
        for j in range(1, len(str_set[1])+1):
            # 一致するときは今いる位置は左上から斜めにjumpできる。
            # なぜなら両文字列で1文字進められるから。
            # そうでなければそのままjを進めるので、そのまま横軸方向に進めるイメージ。
            if str_set[0][i-1] == str_set[1][j-1]:
                # 左上, 左, 上から遷移できる。
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            # 一致しないときは上か左の最大値をそのままもらう程度しかできない
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])
