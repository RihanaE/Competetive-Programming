class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1) ]

        visited = [[0] * len(image[0]) for i in range(len(image))]

        point = image[sr][sc]
        visited[sr][sc] = 1

        def dfs(start_r, start_c):
            image[start_r][start_c] = color

            for row, col in direction:
                new_r = row + start_r
                new_c = col + start_c

                if self.inbound(new_r, new_c, image) and image[new_r][new_c] == point and visited[new_r][new_c] != 1:
                    visited[new_r][new_c] = 1
                    dfs(new_r, new_c)


        dfs(sr, sc)
        return image

    def inbound(self, row, col, image):
        return 0 <= row < len(image) and 0 <= col < len(image[0])