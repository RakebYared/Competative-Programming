class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        def dfs(vertix):
            nonlocal visited

            visited.add(vertix)

            for n in rooms[vertix]:
                if n not in visited:
                    dfs(n)

        dfs(0)
        
        if 0 in visited:
            visited.remove(0)

        return len(visited) == len(rooms) - 1