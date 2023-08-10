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
        
        
        pq = []
        
        for start, end in slots1:
            pq.append((start, end, 1))
        for start, end in slots2:
            pq.append((start, end, 2))
        heapq.heapify(pq)
        
        tstart, tend, tid = heappop(pq)
        while pq:
            
            nstart, nend, nid = heappop(pq)
            #print( tstart, tend, tid, nstart, nend, nid)
            # they ids are same, move on
            if tid == nid:
                tstart = nstart
                tend = nend
                tid = nid
                
                continue
            
            # they intersect
            if tstart <= nstart < tend:
                #find duration of intersection
                intersection = min(tend, nend) - max(nstart, tstart)
                
                # duration qualified
                if intersection >= duration:
                    return [nstart, nstart+duration]
                
                if nend > tend:
                    tstart = nstart
                    tend = nend
                    tid = nid
            # they dont intersect
            else:
                #print('else:', nstart, nend, nid)
                tstart = nstart
                tend = nend
                tid = nid
                #print(tstart, tend, tid)
        
        return []
        