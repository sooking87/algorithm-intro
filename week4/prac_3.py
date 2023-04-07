# 2116313 손수경
# 1번을 해보세요!
def string_matching(T, P):
    for i in range(len(T)):
        if T[i] == P[0]:
            j = 0
            while j != len(P):
                if T[i + j] == P[j]:
                    j += 1
                else:
                    break
            if j == len(P):
                return i
    else:
        return -1


# 2번을 해보세요!
T = input()
P = input()

# 출력합니다!
print(string_matching(T, P))
