from collections import deque
def DepWalk(deps):
    points = set()
    order = []
    connections = {}
    # construct the graph
    for line in deps:
        end = line[0]
        if not end in points:
            points.add(end)
            order.append(end)
            connections[end] = []
        for start in line[1:]:
            if not start in points:
                points.add(start)
                order.append(start)
                connections[start] = []
            if start in connections:
                connections[start] += [end]
            else:
                connections[start] = [end]
    # visit the graph in reverse order
    order.reverse()
    # dfs part
    visited = set()
    ans = deque()
    def dfs(p):
        visited.add(p)
        for neighbor in connections[p]:
            if not neighbor in visited:
                dfs(neighbor)
        ans.appendleft(p)
    for p in order:
        if not p in visited:
            dfs(p)
    return list(ans)

if __name__ == '__main__':
    deps = [[1,2, 3], [2, 4], [3, 5]]
    print(DepWalk(deps))


