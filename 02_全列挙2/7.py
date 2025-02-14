# https://www2.ioi-jp.org/joi/2006/2007-ho-prob_and_sol/2007-ho.pdf#page=5
# output -> 10
"""
基本的な考え方としては、4点を選ぶ必要はなく、
2点をx軸の小さい順から選び、残りの2点をそれ以降で取得し、
存在するかを確認すればよい。
"""

XY = [[9, 4], [4, 3], [1, 1], [4, 2], [2, 4],
      [5, 8], [4, 0], [5, 3], [0, 5], [5, 2]]
# ソートするとX座標が小さい順になる
XY = sorted(XY)
max_value = 0
# 四角形を作るにはあと3点必要
for i in range(len(XY)-3):
    # 四角形を作るにはあと2点必要
    for j in range(i+1, len(XY)-2):
        # 1点目
        x1, y1 = XY[i]
        # 2点目
        x2, y2 = XY[j]
        # ソート済みであるため、x1 < x2 となる
        dx = x2 - x1
        # 1点目が左下、2点目が右上の時
        dy1 = y2 - y1
        # 1点目が左上、2点目が右下の時
        dy2 = y1 - y2

        # 1点目が左下、2点目が右上の時 -> 右下側に2点ある
        # xでソートしているため、左上にはない
        p1 = [x1 + dy1, y1 - dx]
        p2 = [x2 + dy1, y2 - dx]

        # 1点目が左上、2点目が右下の時 -> 右上側に2点ある
        p3 = [x1 + dy2, y1 + dx]
        p4 = [x2 + dy2, y2 + dx]

        if (p1 in XY and p2 in XY) or (p3 in XY and p4 in XY):
            max_value = max(max_value, ((x2-x1)**2+(y2-y1)**2))
print(max_value)
