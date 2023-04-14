# 2116313 손수경
# 1번을 해보세요1
def binary_search(A, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1
    return -1


# 2번을 해보세요!
listA = [int(i) for i in input().split()]
key = int(input())

# 출력합니다!
print("입력 리스트 =", listA)
print("%d 탐색(반복) -->" % (key), binary_search(listA, key, 0, len(listA)-1))
