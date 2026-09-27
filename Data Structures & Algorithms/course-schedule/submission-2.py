class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        memo = {}
        visited = set()
        for c, pre in prerequisites:
            if c not in adjList:
                adjList[c] = []
            if pre not in adjList:
                adjList[pre] = []
            adjList[c].append(pre)

        print(adjList)
        def dfs(val):
            if len(adjList[val]) == 0:
                return True
            if val in memo:
                return memo[val]
            visited.add(val)
            for pre in adjList[val]:
                if pre in visited or not dfs(pre):
                    memo[val] = False
                    return memo[val]
            visited.remove(val)
            memo[val] = True
            return memo[val]

        for prereqs in adjList.values():
            for pre in prereqs:
                if not dfs(pre):
                    return False

        return True
