# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
N = 5
A = [1, 5, 7, 10, 21]
M = 4
B = [2, 4, 17, 8]

Answer = ["No"] * M

for i in range(M):
    b = B[i]
    for j in range(1 << N):
        sum = 0
        is_ok = False
        for k in range(N):
            if j//2**k % 2 == 1:
                sum += A[k]
            if sum == b:
                is_ok = True
        if is_ok:
            Answer[i] = "Yes"
            break

print(Answer)
