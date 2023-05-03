# 2116313 손수경
# 제곱근(sqrt) 함수 사용을 위한 math 모듈
import math

# Euclidean 거리 계산 함수


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


# 억지 기법으로 최근접 쌍의 거리를 구하는 함수
def closest_pair(p):
    n = len(p)              			# 점의 전체 개수
    mindist = float("inf")  			# 최근접 거리 초기화(무한대)
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])  # 유클리드 거리 계산
            if dist < mindist:
                mindist = dist
    return mindist


# 띠 영역에서의 최근접 쌍의 거리를 구하는 함수
def strip_closest(P, d):
    n = len(P)                  # 리스트내의 점의 수
    d_min = d
    P.sort(key=lambda point: point[1])  # y축을 따라 정렬

    for i in range(n):          # y가 최소인 점부터 순서대로
        j = i + 1
        # P[i].y와 P[j].y의 차이가 d_min 이내일 때 까지만 처리
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min                # d_min 반환


# 1번을 해보세요!
def closest_pair_dist(P, n):
    return None


# 2번을 해보세요!
p = []


# 출력합니다!
p.sort(key=lambda point: point[0])
print("가장 가까운 두 점의 거리", closest_pair_dist(p, len(p)))
