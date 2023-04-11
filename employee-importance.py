"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        
    
        for i in employees:
            graph[i.id].append(i.subordinates)
            graph[i.id].append(i.importance)

        visited = set()
        importance = graph[id][1]
        

        def dfs(node, graph):
            nonlocal importance

            if node in visited:
                return

            visited.add(node)

            for i in graph[node][0]:
                if i not in visited:
                    importance += graph[i][1]
                    dfs(i, graph)

        dfs(id, graph)
        return importance