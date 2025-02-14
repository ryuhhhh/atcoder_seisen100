# https://atcoder.jp/contests/abc095/tasks/arc096_a

A = 1500
B = 2000
C = 1900

X = 3
Y = 2

C *= 2  # A,B 1枚分に
A_and_B = A + B

sum = 0

# XとYのうち少ない方で共通で買えるだけ買う
# ABピザの方が安いならABピザで買えるまで買う
if A_and_B > C:
    sum += C * min(X, Y)
# AとBピザ合わせた方が安いならAとBピザで買えるまで買う
else:
    sum += A_and_B * min(X, Y)

# 残りは少ないほうで
if X > Y:
    remain = X - Y
    # A1枚よりAB2枚の方が安いケース(リアルだったらありえない)
    if A > C:
        sum += remain * C
    else:
        sum += remain * A
else:
    remain = Y - X
    # B1枚よりAB2枚の方が安いケース(リアルだったらありえない)
    if B > C:
        sum += remain * C
    else:
        sum += remain * B

print(sum)
