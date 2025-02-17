# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
# フィボナッチ数列とは、以下の漸化式で定義される数列。(問題文ver)
# 0から始まっている。
# F0 = 1
# F1 = 1
# Fi = Fi-1 + Fi-2 (i >= 2)
n = int(input())


def fibonacci(n):
    # n+1とするのは、問題ではn=0から始まるため
    fib = [0] * (n+1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n-1]


# テスト例
print(f"フィボナッチ数F({n}) = {fibonacci(n)}")
