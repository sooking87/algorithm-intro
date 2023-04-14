# 2116313 손수경
# 1번을 해보세요!
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
        printStep(A, i)

# 중간 과정을 출력하는 함수에요!


def printStep(arr, val):
    print("  Step %2d = " % val, end='')
    print(arr)


# 2번을 해보세요!
data = [int(i) for i in input().split()]

# 출력합니다!
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)
