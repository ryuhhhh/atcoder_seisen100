# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp
"""
データの与え方が特殊
 1
0 1
 0
1 0
 1
なら、
212
0x1
202
1x0
212
となるイメージ。つまり壁を1マスとしてマップを作る。
ただし、
0: 壁がない通路
1: 壁がある通路(通れない)
2: 本当のマス
x: 本当は存在しないマス(便宜上作るがどのみち周囲に止まれるマスがないので2で置く)
"""
while True:
    W, H = map(int, input().split())
    if (W, H) == (0, 0):
        exit()
    # 壁を考慮して2*H-1, 2*W-1の迷路を作成
    maze = [[0 for _ in range(2*W-1)] for _ in range(2*H-1)]

    # マスの情報を入力
    for row in range(2*H-1):
        # 空白を取り除いて、1文字ずつ取り出す、ただしintにして配列に
        line = list(map(int, input().replace(" ", "")))
        for column in range(2*W-1):
            # 普通のマス
            if (row % 2 == 0 and column % 2 == 0) or\
                    (row % 2 == 1 and column % 2 == 1):
                maze[row][column] = 2
            # 壁マス
            else:
                maze[row][column] = line[column//2]
    # mazeにdistを直接書き込むのだが、0や1で初期化すると壁マスとの区別がつかないので、1001で初期化
    stack = [[0, 0, 1001]]
    while stack:
        row, column, dist = stack.pop(0)
        wall_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for wd in wall_directions:
            wrow = row + wd[0]
            wcolumn = column + wd[1]
            # 迷路の範囲外なら何もできない
            if not (0 <= wrow < 2*H-1) or not (0 <= wcolumn < 2*W-1):
                continue
            # 壁になっているなら何もできない
            if maze[wrow][wcolumn] == 1:
                continue
            # 壁がないなら、壁マスを通り越して、次に進む
            else:
                # 壁を通り越して進む
                nrow = row + wd[0]*2
                ncolumn = column + wd[1]*2
                if 0 <= nrow < 2*H-1 and 0 <= ncolumn < 2*W-1 and\
                        maze[nrow][ncolumn] == 2:
                    maze[nrow][ncolumn] = dist+1
                    stack.append([nrow, ncolumn, dist+1])

    print(maze[-1][-1]-1000 if maze[-1][-1] != 2 else 0)
