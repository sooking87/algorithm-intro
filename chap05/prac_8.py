# 2116313 손수경
# 1번을 해보세요!
def multiply(A, B, C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]


# 2번을 해보세요!
A = []
B = []
n = int(input())
C = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    a, b = input().split()
    temp = [int(a), int(b)]
    A.append(temp)
for i in range(n):
    a, b = input().split()
    temp = [int(a), int(b)]
    B.append(temp)

# 출력합니다!
multiply(A, B, C)
print(C)
