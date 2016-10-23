def mix(s1, s2):
    
    alph = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    dict1 = {i : s1.count(i) for i in alph}
    dict2 = {i : s2.count(i) for i in alph}
    
    list1 = []
    
    for i in alph:
        if max(dict1[i], dict2[i]) > 1:
            list1.append([max(dict1[i], dict2[i]), '', i, ''])
            if dict1[i] == dict2[i]:
                list1[len(list1)-1][1] = '=:' + i * dict1[i]
                list1[len(list1)-1][3] = 1
                
            elif dict1[i] > dict2[i]:
                list1[len(list1)-1][1] = '1:' + i * dict1[i]
                list1[len(list1)-1][3] = 3
                
            elif dict1[i] < dict2[i]:
                list1[len(list1)-1][1] = '2:' + i * dict2[i]
                list1[len(list1)-1][3] = 2
                
    list1.sort(key = lambda x : (x[0], x[3]), reverse = True)
    
    return "/".join([a[1] for a in list1])