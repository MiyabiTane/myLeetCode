from collections import deque

def canFinish(numCourses, prerequisites):
    visited = [0 for _ in range(numCourses)]
    #自分より後ろにある頂点
    node = [[] for _ in range(numCourses)]
    for pre, nex in prerequisites:
        node[pre].append(nex)

    def dfs(u):
        #トポロジカルソート中に自分に戻ってきてしまった時
        if visited[u] == -1:
            return False
        if visited[u] == 1:
            return True
        visited[u] = -1
        for n in node[u]:
            #どこかでループができたら終了
            if not dfs(n):
                return False
        visited[u] == 1
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


ans = canFinish(2, [[1, 0], [0, 1]])
print(ans)
