from __future__ import annotations
def is_blocked(required_tasks, task_from, task_to):
    required_tasks = set(required_tasks)
    new_from, new_to = [], []
    graph = {}
    for f, t in zip(task_from, task_to):
        if f in required_tasks:
            new_from.append(f)
            new_to.append(t)
            graph[f] = graph.get(f, []) + [t]
    visited = set()
    sorted_task = []
    def top_sort(task):
        visited.add(task)
        sorted_task.append(task)
        for nb in graph.get(task, []):
            if not nb in visited:
                top_sort(nb)
    [top_sort(t) for t in required_tasks if not t in visited]
    def dfs(task):
        visiting.add(task)
        for nb in graph.get(task, []):
            if nb in visiting: return True
            if not nb in visited and dfs(nb):
                return True
        visited.add(task)
        visiting.remove(task)
        return False
    visited, visiting = set(), set()
    for t in sorted_task:
        if not t in visited and dfs(t): return True
    return False





if __name__ == '__main__':
    required_tasks = ["get gas", "drive", "load materials", "exit"]
    task_from = ["get gas", "drive", "load materials"]
    task_to = ["drive", "exit", "exit"]
    print(is_blocked(required_tasks, task_from, task_to))
    required_tasks = ["get gas", "drive", "exit"]
    task_from = ["get gas", "drive", "load materials", "exit"]
    task_to = ["drive", "exit", "exit", "load materials"]
    print(is_blocked(required_tasks, task_from, task_to))

