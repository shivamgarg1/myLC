class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rcount = 0
        dcount = 0
        for char in senate:
            if char == 'R':
                rcount += 1
            else:
                dcount += 1
        
        num_d_ban = 0
        num_r_ban = 0
        
        q = deque(senate)
        
        while rcount and dcount:
            top = q.popleft()
            
            if top == 'R':
                if num_r_ban:
                    num_r_ban -= 1
                    rcount -= 1
                else:
                    num_d_ban += 1
                    q.append(top)
            else:
                if num_d_ban:
                    num_d_ban -= 1
                    dcount -= 1
                else:
                    num_r_ban += 1
                    q.append(top)
        
        return 'Radiant' if rcount else 'Dire'