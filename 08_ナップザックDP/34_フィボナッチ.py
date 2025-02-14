n = int(input())


def fibonacci(n):
    fib = [0] * (n + 1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


# テスト例
print(f"フィボナッチ数F({n}) = {fibonacci(n)}")
