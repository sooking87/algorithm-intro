# 2116313 손수경
# 1번을 해보세요!
def fib_iter(n):
    # for문을 이용해보세요!
    if n < 2:
        return n
    last = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += last
        last = tmp
    return current


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(fib_iter(n))
