# 2116313 손수경
# 1번을 해보세요!
def selection_sort(A):
    # 여기에 코드를 작성해보세요!
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        printStep(A, i + 1)


def printStep(arr, val):
    print("  Step %2d = " % val, end='')
    print(arr)


# 2번을 해보세요!
A = [int(i) for i in input().split()]

# 출력합니다!
print("Original  :", A)
selection_sort(A)
print("Selection :", A)
