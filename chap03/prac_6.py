# 2116313 손수경
# 필요한 모듈을 추가해 보세요!
import queue
# 1번을 해보세요!


def bfs(graph, start):
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)

    return None


# 2번을 해보세요!
n = int(input())
mygraph = dict()
for i in range(n):
    a, b = input().split()
    mygraph[a] = mygraph.setdefault(a, set()) | {b}
    mygraph[b] = mygraph.setdefault(b, set()) | {a}

# 출력합니다!
print('BFS : ', end='')
bfs(mygraph, "A")
print()
