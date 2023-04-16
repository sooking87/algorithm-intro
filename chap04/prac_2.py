# 2116313 손수경
# 1번을 해보세요!
def topological_sort(graph):
    inDeg = {}
    # 차수 setting
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1

    # 차수가 0인 리스트 setting
    vList = []
    for v in graph:
        if inDeg[v] == 0:
            vList.append(v)

    while len(vList) != 0:
        v = vList.pop()
        print(v, end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vList.append(u)


# 2번을 해보세요!
mygraph = dict()
n1 = int(input())
for i in range(n1):
    mygraph.setdefault(chr(ord('A') + i), set())

n2 = int(input())
for i in range(n2):
    a, b = input().split()
    mygraph[a] |= {b}


# 출력합니다!
print('topological_sort: ')
topological_sort(mygraph)
print()
