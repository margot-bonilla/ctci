from typing import List


def buildOrder(n: int, dependencies: List[List[int]]) -> List[int]:
    graph = dict()
    for i in range(n):
        graph[i] = []

    for item in dependencies:
        graph[item[0]].append(item[1])

    stack = []
    rec = [False] * (n + 1)
    visited = [False] * (n + 1)

    for v in range(n):
        if not visited[v]:
            if isCycle(v, graph, stack, visited, rec):
                return []

    if len(stack) == n:
        return stack

    return []


def isCycle(v, graph, stack, visited, rec):
    rec[v] = True
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            if isCycle(node, graph, stack, visited, rec):
                return True
        elif rec[node]:
            return True

    stack.insert(0, v)

    rec[v] = False
    return False


def test():
    print(buildOrder(4, [[0, 1], [1, 2], [2, 3]]))
    print(buildOrder(4, [[0, 1], [1, 2], [2, 3], [0, 3]]))


if __name__ == "__main__":
    test()
