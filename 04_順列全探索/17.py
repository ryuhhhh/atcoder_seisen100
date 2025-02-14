# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
import itertools
# 8クイーン問題は、順列を作成して、それが条件を満たすかを確認していくだけで解ける
# 特に難しいのはis_valid関数で、斜めにクイーンがないかを確認する処理

k = 2
positions = [
    [2, 2],
    [5, 3]
]

board = [["."] * 8 for _ in range(8)]


def print_board(board):
    for row in board:
        print("".join(row))


def is_valid(board):
    """
    完成された盤面で縦横斜めにクイーンが重なっていないかを確認する
    """
    for i in range(8):
        for j in range(8):
            if board[i][j] == "Q":
                # 直積で全探索
                for r, c in itertools.product(range(8), repeat=2):
                    # r + c == i + j は右下がりの斜め
                    # r - c == i - j は右上がりの斜め
                    if (r == i or c == j or r + c == i + j or r - c == i - j)\
                            and board[r][c] == "Q" and (r != i or c != j):
                        return False
    return True


for rows in itertools.permutations(range(8)):
    # enumerate(rows)で行番号と列番号を取得しそこにクイーンを配置する
    # つまり、(0, rows[0]), (1, rows[1]), ... となる
    for r, c in enumerate(rows):
        board[r][c] = "Q"

    # 問題より指定された位置にクイーンがあるかを確認
    is_continue = False
    for position in positions:
        r, c = position
        if board[r][c] != "Q":
            is_continue = True
    if is_continue:
        for r, c in enumerate(rows):
            board[r][c] = "."
        continue

    if is_valid(board):
        print_board(board)
        break

    # もとに戻す
    for r, c in enumerate(rows):
        for position in positions:
            if r == position[0]:
                continue
        board[r][c] = "."
