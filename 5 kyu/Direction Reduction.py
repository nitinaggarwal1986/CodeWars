def dirReduc(arr):
    temp = "|".join(arr)
    irr = ['NORTH|SOUTH', 'SOUTH|NORTH', 'EAST|WEST', 'WEST|EAST']
    
    while(sum(temp.count(a) for a in irr) != 0):
        for a in irr:
            temp = temp.replace(a, "").replace("||", "|")
    
    result = temp.split('|')
    result = [x for x in result if x != ""]
    
    return result