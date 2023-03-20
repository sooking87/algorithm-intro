# IT공학전공 2116313 손수경
# 1번을 해보세요!
A = [int(n) for n in input().split()]

# 2번을 해보세요!


def unique_elements(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                return False
    return True


# 출력합니다!
print(unique_elements(A))
