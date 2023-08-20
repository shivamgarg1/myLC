class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.visited = set()
        self.stack = {}
        self.max_stack_size = -1
        def dfs(node, rec_depth):
            if node in self.visited:return False
            if node in self.stack:
                self.max_stack_size = max(self.max_stack_size, rec_depth - self.stack[node] + 1)
                return True
            
            if edges[node] == -1:return False
            self.stack[node] = rec_depth + 1
            dfs(edges[node], rec_depth + 1)
            self.stack.pop(node)
            self.visited.add(node)
            return False
        
        for i in range(len(edges)):
            if edges[i] != -1 and i not in self.visited:
                dfs(i, 0)
        return self.max_stack_size