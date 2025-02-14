N, K = map(int, input().split())
A = {}
# dp[日にち][昨日のパスタ][一昨日のパスタ]
dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]

for _ in range(K):
    day, pasta = map(int, input().split())
    A[day-1] = pasta

if 0 in A:
    for pasta0 in range(3):
        for pasta1 in range(3):
            dp[0][0][0] = 1

for day in range(1, N-1):
    # 明日
    for pasta0 in range(3):
        # 当日
        for pasta1 in range(3):
            if day in A and A[day] != pasta1:
                continue
            # 昨日
            for pasta2 in range(3):
                if pasta0 != pasta1 or pasta1 != pasta2:
                    dp[day+1][pasta0][pasta1] += dp[day][pasta1][pasta2]
print(dp)
