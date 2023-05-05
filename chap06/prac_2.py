# 2116313 손수경
# 1번을 해보세요!
def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL

    for i in A:
        count[i] += 1
    for i in range(MAX_VAL):
        count[i] += count[i - 1]
    for i in range(len(A)):
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
    for i in range(len(A)):
        A[i] = output[i]


# 2번을 해보세요!
data = [int(i) for i in input().split()]


# 출력합니다!
MAX_VAL = 10
print("Original  : ", data)
counting_sort(data)             # 카운팅 정렬
print("Counting  : ", data)
