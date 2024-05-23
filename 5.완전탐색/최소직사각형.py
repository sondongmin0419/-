def solution(sizes):
    answer = 0
    L_size = 0
    S_size = 0
    for size in sizes:
      l_size = max(size)
      s_size = min(size)
      if (L_size <= l_size):
        L_size = l_size
      if (S_size <= s_size):
        S_size = s_size
    answer = L_size * S_size
        
    print(answer)
    return answer
  
solution([[60, 50], [30, 70], [60, 30], [80, 40]]	)