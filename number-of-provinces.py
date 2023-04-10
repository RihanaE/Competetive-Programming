class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()  # Initialize visited set
        
        # Define depth-first search (dfs) function
        def dfs(isConnected, visited, i):
            if i in visited:  # If already visited, return 0
                return 0
            visited.add(i)  # Add i to visited set
            for j in range(len(isConnected[i])):  # Check for direct connections
                if isConnected[i][j] == 1:
                    dfs(isConnected, visited, j)  # Recursively call dfs on j
            return 1  # Return 1 to represent current province
        
        provinces = 0  # Initialize provinces count
        for i in range(len(isConnected)):  # Loop through all cities
            provinces += dfs(isConnected, visited, i)  # Call dfs on city i and add result to provinces
        return provinces  # Return total number of provinces
2
2


        # arr = []
        # graph = defaultdict(list)
        # for row in range(1, len(isConnected) + 1):
        #     for col in range(1, len(isConnected[0]) + 1):
        #         if isConnected[row - 1][col - 1] == 1 :
        #             graph[row].append(col)
        #             arr.append(row)

        #         if len(graph[row]) > 1:
        #             if row in graph[row]:
        #                 graph[row].remove(row)

        
        
        # visited = set()
        # count = 0

        # def dfs( point, graph):
        #     stack = [point]
        #     visited = set()

        #     while stack:
        #         node = stack.pop()
                
        #         for i in graph[node]:
        #             if i not in visited:
        #                 visited.add(i)
        #                 stack.append(i)

        #     return visited

        # for i in arr:
        #     if i not in visited:
                
        #         visited = dfs(i, graph)
        #         count += 1
               
                
        
        # return count