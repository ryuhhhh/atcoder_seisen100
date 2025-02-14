# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
M = 5
AX = [8, 6, 4, 7, 0]
AY = [5, 4, 3, 10, 10]

X = [10, 2, 9, 8, 10, 1, 8, 6, 6, 0]
Y = [5, 7, 7, 10, 2, 2, 1, 7, 0, 9]
XY = []
for i in range(len(X)):
    XY.append([X[i], Y[i]])
# x座標が小さい順にソート
XY = sorted(XY)

# 探している星の1番左にある星を基準にする
min_pos = AX.index(min(AX))

# 探している星の相対位置を求める
positions = []
for i in range(len(AX)):
    if i == min_pos:
        continue
    positions.append([AX[i]-AX[min_pos], AY[i]-AY[min_pos]])

# 最低でもM-1個は右側に必要
for i in range(len(XY)-(M-1)):
    # 左から順に基準の星を決める
    x_, y_ = XY[i]

    exist = True
    # 探している星の相対位置から、他の星が存在するか確認
    for position in positions:
        # 1つでも存在しなければスキップ
        if [x_+position[0], y_+position[1]] not in XY:
            exist = False
            break

    if exist:
        print(x_-AX[min_pos], y_-AY[min_pos])
        exit()
