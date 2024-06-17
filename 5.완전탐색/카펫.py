def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    # x * y = brown + yellow
    # (x+y)*2 -4  = brown
    # x + y = brown/2 +2
    for i in range(3, int((brown/2 +2)/2) +1):
        y = i
        x = int(brown/2) + 2 - i
        if x*y == brown+yellow:
            answer = [x,y]
            break
    print(answer)
    
            
        
        
    
    return answer

solution(10,2)