def runoff(voters):
    
    do = True
    removed = []
    
    while (do): 
        voters = [[v for v in x if v not in removed] for x in voters]
        candidates = []
        for x in voters:
            for c in x:
                if c not in candidates:
                    candidates.append(c)
        
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) == 0:
            return None
        
        counts = {x : [v[0] for v in voters].count(x) for x in candidates}
        
        maxCount = max(counts.values())
        
        if 2 * maxCount > len(voters):
            do = False
            return list(counts.keys())[list(counts.values()).index(maxCount)]
        else:
            minCount = min(counts.values())
            for x in counts.keys():
                if counts[x] == minCount:
                    removed.append(x)