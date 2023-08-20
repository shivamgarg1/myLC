class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        frequencies = [0] * 26
        for char in tasks:
            frequencies[ord(char) - ord('A')] += 1
        
        frequencies.sort()
        max_f = frequencies.pop()
        
        max_idle_time = (max_f - 1 ) * n
        
        while frequencies and max_idle_time > 0 :
            max_idle_time -= min(max_f-1, frequencies.pop())
        
        max_idle_time = max(0, max_idle_time)
        return max_idle_time + len(tasks)