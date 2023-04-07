# 2116313 손수경
# 1번을 해보세요!
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)
    return None


# 2번을 해보세요!
n = int(input())
mygraph = dict()
temp_list = [[i for i in input().split()[:2]] for _ in range(n)]
for i in range(n):
    mygraph[temp_list[i][0]].append(temp_list[i][1])
print(mygraph)


# 출력합니다!
print('DFS : ', end='')
dfs(mygraph, "A", set())
print()
