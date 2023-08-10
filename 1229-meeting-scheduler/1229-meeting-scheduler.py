class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        '''
        
        1)              _______________
        2) ______   _________      ____________      _________
        
        [1,5]
        [5, 6] duration = 1units
            
        1) sort both slots
        2) initilaize 2 indexes i/j to 0
        3) iterate on on slots1
            4) find intersection: end 
        
        [[10,50],[60,120],[140,210]]
        [[0,15],[60,70]]
        8
        
        [(0, 15, 2), (10,50, 1), (60, 120, 1), (60, 70, 2)]        
        
        
        
        [[0,1],[100,1000100]]
        [[90,1000100],[0,2]]
        1000000
        
        
        (0, 1, 1), (0, 2, 2), (90, 1000100,2), (100, 1000100, 1)
        
        '''
        
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []