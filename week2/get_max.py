# IT공학전공 2116313 손수경
# 1번을 해보세요!
def find_max(A):
    max = A[0]
    # for i in range(1, len(A)):
    #     temp = A[i]
    #     if temp > max:
    #         max = temp
    for i in A[1:]:
        if i > max:
            max = i
    return max


# 2번을 해보세요!
array = [int(n) for n in input().split()]

# 출력합니다!
print(array, "최댓값=", find_max(array))
