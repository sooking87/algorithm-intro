# 2116313 손수경
# 1번을 해보세요!
def bino_coef_dc(n, k):
    if k == 0 or k == n:
        return 1
    return bino_coef_dc(n - 1, k - 1) + bino_coef_dc(n - 1, k)


# 2번을 해보세요!
n = int(input())
k = int(input())


# 출력합니다!
print("C(%d,%d) =" % (n, k), bino_coef_dc(n, k))
