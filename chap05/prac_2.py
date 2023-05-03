# 2116313 손수경
# 1번을 해보세요!
def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid - 1)
        quick_sort(A, mid + 1, right)


# 2번을 해보세요!
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and pivot >= A[low]:
            low += 1
        while high >= left and pivot < A[high]:
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high


# 3번을 해보세요!
data = [int(i) for i in input().split()]


# 출력합니다!
print("Original  : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
