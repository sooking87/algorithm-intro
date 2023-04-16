# 2116313 손수경
# 필요한 모듈을 추가해 보세요!

# 1번을 해보세요!
def closest_pair(p):
    distance = float('Inf')
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            temp_dis = (((p[i][0] - p[j][0]) ** 2) +
                        ((p[i][1] - p[j][1]) ** 2)) ** 0.5
            if distance > temp_dis:
                distance = temp_dis

    return distance


# 2번을 해보세요!
n = int(input())
p = [tuple(int(i) for i in input().split()[:2]) for j in range(n)]

# 출력합니다!
print("최근접 거리:", closest_pair(p))
