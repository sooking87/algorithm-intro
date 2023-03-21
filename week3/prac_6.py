# 2116313 손수경
# 1번을 해보세요!
def binary_digits(n):
    count = 1
    while n > 1:
        count += 1
        n = n // 2
    return count


# 2번을 해보세요!
n = int(input())

# 출력합니다!
print(binary_digits(n))


'''
# 나눠서 구하는 것이 아니라 result에서 2씩 곱해가면서 n보다 크거가 같아지는 횟수를 구하는 식으로 생각할 수 있다.

def binary_digits(n):
    k = 1
    cnt = 0
    while k <= n:
        cnt += 1
        k *= 2
    return cnt


n = int(input())

print(binary_digits(n))
'''
