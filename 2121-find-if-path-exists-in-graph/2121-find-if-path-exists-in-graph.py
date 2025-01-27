class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # DFS with recursion

        if source == destination:
            return True

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Graph Ex visualization: graph = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [3, 1]}

        seen = set()
        seen.add(source) # Mark source as seen

        def dfs(i):
            if i == destination:
                return True
            
            for nei_node in graph[i]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            return False
        
        return dfs(source)

