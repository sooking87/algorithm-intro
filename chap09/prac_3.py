# 2116313 손수경
# 1번을 해보세요!
def isSafe( maze, x, y, mark ):
    W, H = len(maze[0]), len(maze)
    if x>=0 and x<W and y>=0 and y<H:
        if maze[y][x]!=0 and mark[y][x]==0:
            return True
    return False
def solve_maze( maze, x, y ):
    W, H = len(maze[0]), len(maze)                  # 미로 맵의 크기
    sol = [[0 for j in range(W)] for i in range(H)] # 해 경로 맵
    mark= [[0 for j in range(W)] for i in range(H)] # 방문 맵
    if DFS_maze(maze, x, y, sol, mark) == False:   # 탐색 실패
        print("출구를 찾을 수 없음") 
    else :                               # 탐색 성공
        for i in sol: print(i)               # 해 경로 맵 출력
def DFS_maze(maze, x, y, sol, mark):
    W, H = len(maze[0]), len(maze)
    if not isSafe(maze, x, y, mark):
        return False
    mark[y][x]=1
    sol[y][x]=1
    if maze[y][x]==2: return True
    if DFS_maze(maze, x+1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y+1, sol, mark)==True: return True
    if DFS_maze(maze, x-1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y-1, sol, mark)==True: return True
    sol[y][x]=0
    return False
x,y = list(map(int, input().split()))
# 출력합니다!
maze = [ [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
         [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solve_maze(maze, x, y) 