def solution(digits):
    greatest = 0
    
    for i in range(len(digits)-4):
        temp = int(digits[i:i+5])
        if temp > greatest:
            greatest = temp
        
    return greatest