def find_nb(m):
    volume = 0
    n = 1
    while volume < m:
        volume += n ** 3
        if volume == m:
            return n
        n += 1
    
    return -1