class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        element = set()
        graph = defaultdict(list)

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            element.add(i[0])
            element.add(i[1])

        for i in range(1, len(edges) + 2):
            if len(graph[i]) == len(element) - 1:
                return i