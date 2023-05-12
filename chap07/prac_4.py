# 2116313 손수경
# 1번을 해보세요!
def bino_coef_dp(n, k):
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


# 2번을 해보세요!
n = int(input())
k = int(input())


# 출력합니다!
print("C(%d,%d) =" % (n, k), bino_coef_dp(n, k))
