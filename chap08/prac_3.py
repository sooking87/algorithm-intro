# 2116313 손수경
INF = 9999


# 1번을 해보세요!
def getMinVertex(dist, selected) :
    minv = -1   
    mindist = INF
    # 코드를 추가해보세요!
    for v in range(len(dist)):
        if not selected[v] and dist[v]<mindist:
            mindist= dist[v]
            minv=v
    return minv

# 2번을 해보세요!
def MSTPrim(vertex, adj) :
    vsize=len(vertex)
    dist=[INF]*vsize
    dist[0]=0

    selected = [False] * vsize
    for i in range(vsize):
        u=getMinVertex(dist, selected)
        selected[u]=True
        print(vertex[u], end=':')
        print(dist)

        for v in range(vsize):
            if(adj[u][v] != None):
                if selected[v]==False and adj[u][v]<dist[v]:
                    dist[v]=adj[u][v]
                    
# 3번을 해보세요!
vertex = [i for i in input().split()]
n = int(input())
weight = [[INF] * len(vertex) for _ in range(len(vertex))]
for _ in range(n):
    v1, v2, w = [m for m in input().split()]
    i = vertex.index(v1)
    j = vertex.index(v2)
    weight[i][j] = int(w)
    weight[j][i] = int(w)

print(weight)
print(vertex)

# 출력합니다!
print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)