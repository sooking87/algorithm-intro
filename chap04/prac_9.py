# 2116313 손수경
# 1번을 해보세요!
def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if pos + 1 == left + k:
        return A[pos]
    elif pos + 1 > left + k:
        return quick_select(A, left, pos - 1, k)
    elif pos + 1 < left + k:
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))

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
array = [int(i) for i in input().split()]
k = int(input())

# 출력합니다!
n = len(array)
print("입력 리스트 =", array)
print("[축소정복] %d번째 작은 수: " % (k), quick_select(array, 0, n-1, k))
