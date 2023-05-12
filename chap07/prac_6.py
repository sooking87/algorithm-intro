# 2116313 손수경
# 1번을 해보세요!
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                A[i][w] = A[i - 1][w]
            else:
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][W]


# 2번을 해보세요!
n = int(input())
val = [int(i) for i in input().split()]
wt = [int(i) for i in input().split()]
W = int(input())


# 출력합니다!
print("최대 가치:", knapSack_dp(W, wt, val, n))
