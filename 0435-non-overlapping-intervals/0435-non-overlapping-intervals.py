class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        
        ____________
            _____________
              _______________
              
              
              
        ___________________________
           
           --- -----  ------  ---------
           
       ____________
                ____X________  ____________
                
    
        _______X____
          ___  ___   ___________
        
        
        algo:
        1) sort the intervals based on start time values
        2) iterate and compare i and i+1 interval
             - increment counter for the interval which has higher end time
            - subsequently make other as last time interval
        3) return the counter
        
        
        Space: Considering in place sort -> O(1)
        Time: O(N log N)
        
        [[0,2],[1,3],[2,4],[3,5],[4,6]]
        
        
        
        
        '''
        
        intervals = sorted(intervals, key = lambda x:x[0])
        last_start, last_end = intervals[0]
        count = 0
        for start, end in intervals[1:]:
            if last_start <= start < last_end:
                count += 1
                if last_end > end:
                    last_start = start
                    last_end = end
            else:
                last_start = start
                last_end = end
        
        return count
        
        