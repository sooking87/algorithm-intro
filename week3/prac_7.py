# 2116313 손수경
# 1번을 해보세요!
def factorial(n):
    # 종료 조건
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(factorial(n))

'''
재귀함수 -> 자기 자신을 부르는 것 -> 반드시 종료 조건이 필요
'''
