# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
N = 19
S = "3141592653589793238"

# N = int(input())
# S = input()

count = 0
# setを使うことで重複を.add()するだけで防ぐ
result = set()

# 1文字目を見つける
for i in range(10):
    position1 = S.find(str(i))
    if position1 == -1:
        continue
    # 2文字目を見つける
    for j in range(10):
        # 1文字目以降で探す
        # returnは  position1以降の文字列   での位置
        position2 = S[position1 + 1:].find(str(j))
        if position2 == -1:
            continue
        # 3文字目を見つける
        for k in range(10):
            # 2文字目以降で探す
            position3 = S[position1 + 1 + position2 + 1:].find(str(k))
            if position3 == -1:
                continue
            result.add((i, j, k))

print(len(result))
