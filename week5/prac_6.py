# 2116313 손수경
# 1번을 해보세요!
def power(x, n):
    # 순환 구조로
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)


# 2번을 해보세요!
x = int(input())
n = int(input())

# 출력합니다!
print("축소정복기법(%d**%d) =" % (x, n), power(x, n))
