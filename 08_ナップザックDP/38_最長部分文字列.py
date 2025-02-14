# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
n = int(input())
S = []
for i in range(n):
    inner = []
    for j in range(2):
        inner.append(input())
    S.append(inner)


for s in S:
    dp = [[0 for _ in range(len(s[1])+1)] for _ in range(len(s[0])+1)]
    # 0番目は何も選択しないを表すためスキップ
    for i in range(1, len(s[0])+1):
        # 0番目は何も選択しないを表すためスキップ
        for j in range(1, len(s[1])+1):
            # 一致するときは斜めにjumpできる
            if s[0][i-1] == s[1][j-1]:
                # iとjが一致しているならi-1文字目とj-1文字目から1つ値を加えたカウントにできる
                # 斜めに移動できるけど他のスタート地点によってはほかの値のほうが大きい場合がある
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            # 一致しないときは上か左の最大値をそのままもらう程度しかできない
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for r in dp:
        print(r)
    print()
