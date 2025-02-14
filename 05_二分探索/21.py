# https://atcoder.jp/contests/abc023/tasks/abc023_d
# スコアを2分探索して実現可能な高度を探すイメージ
# スコアx+1では可能だがスコアxでは無理という値を探す
N = 4  # 風船の数=かかる時間の秒数
A = [
    [5, 6],
    [12, 4],
    [14, 7],
    [21, 2]
]

N = 6
A = [[100, 1,],
     [100, 1,],
     [100, 1,],
     [100, 1,],
     [100, 1,],
     [1, 30,]]

# 高度のリミット
left, right = 0, 10**10

# 探索範囲が1要素に絞られるまで続けるため<=とする
while left <= right:
    target_height = (left+right)//2  # 探索する高度
    time_limits = []
    for i in range(N):
        # 各風船をその高度で割るにはいつまでに割ればいいかの秒数
        # つまり期限
        # (指定高度-風船の初期高度)/風船の上昇速度
        time_limits.append((target_height-A[i][0])//A[i][1])
    # 期限が早い順
    time_limits = sorted(time_limits)

    # 各風船は期限が早い順にその秒数以内でないといけない
    ok = True
    # tは期限を表す
    for t in range(N):
        # t以内に割れない風船がある場合はその高度は無理
        if time_limits[t] < t:
            ok = False
            break

    # 割れるのならもっと低くてもよい
    if ok:
        right = target_height - 1
    # 割れないならもっと高く設定する
    else:
        left = target_height + 1

print(left)
