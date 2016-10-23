class User:
    ranks = [x for x in range(-8, 9) if x != 0]
    
    def __init__(self):
        self.rankInd = 0
        self.rank = User.ranks[self.rankInd]
        self.progress = 0
    
    def inc_progress(self, rankAct):
        temp = User.ranks.index(rankAct) - User.ranks.index(self.rank)
        temp1 = self.progress
        if temp > 0:
            self.progress += temp * temp * 10
        elif temp == 0 :
            self.progress += 3
        elif temp == -1:
            self.progress += 1
        
        if self.rank == 8:
            self.progress = temp1
        
        if self.progress > 100:
            inc = int(self.progress / 100)
            self.rankInd += inc
            if self.rankInd < len(User.ranks):
                self.rank = User.ranks[self.rankInd]
                self.progress -= 100 * inc
        if self.rank == 8:
            self.progress = 0