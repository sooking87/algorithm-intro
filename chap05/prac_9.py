# 2116313 손수경
import numpy as np


# 1번을 해보세요!
def strassen(A, B):
    n = len(A)
    if n == 1:
        return A * B
    n2 = n // 2
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:]
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:]

    M1 = strassen(A11+A22, B11+B22)
    M2 = strassen(A21+A22, B11)
    M3 = strassen(A11, B12-B22)
    M4 = strassen(A22, B21-B11)
    M5 = strassen(A11+A12, B22)
    M6 = strassen(A21-A11, B11+B12)
    M7 = strassen(A12-A22, B21+B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


# 2번을 해보세요!
A = []
B = []
n = int(input())
for i in range(n):
    a, b = input().split()
    temp = [int(a), int(b)]
    A.append(temp)
for i in range(n):
    a, b = input().split()
    temp = [int(a), int(b)]
    B.append(temp)
A = np.array(A)
B = np.array(B)


# 출력합니다!
C = strassen(A, B)
print(C)
