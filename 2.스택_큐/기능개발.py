def solution(progresses, speeds):
    answer = []
    p_num = 0
    p_cnt = 0
    while p_num < len(progresses) and progresses[p_num]<100:
      for idx in range(p_num,len(speeds)):
        progresses[idx] += speeds[idx]
      if progresses[p_num] >= 100:
        while p_num < len(progresses) and progresses[p_num] >= 100:
          p_num +=1
          p_cnt +=1
        answer.append(p_cnt)
        p_cnt = 0
    print(answer)
        
        
        
    return answer
  
solution([93, 30, 55]	,[1, 30, 5])
solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1])