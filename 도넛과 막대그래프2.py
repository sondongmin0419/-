def solution(edges):
    answer = [0,0,0,0]
    edge_list = [[] for i in range(len(edges)+1)]
    find_edge = 0
    cnt_edge = 0
    for edge in edges:
      edge_list[edge[0]].append(edge[1])
      if len(edge_list[edge[0]])> cnt_edge:
        find_edge = edge[0]
        cnt_edge = len(edge_list[edge[0]])
    print(find_edge)
    print(cnt_edge)
    print(edge_list)
    answer[0] = find_edge
    answer[2] = len(edge_list[find_edge])
    for idx in range(len(edge_list)):
      if edge_list[idx] ==[]:
        continue
      if idx == find_edge:
        continue
      if idx in edge_list[idx]:
        answer[1]+=1
        continue
      _line_cnt = 0
      checked_edge_list = [idx]
      checked_edge_list.extend(edge_list[idx])
      _edge_list = []
      _edge_list.extend(edge_list[idx])
      check_8 = False
      _line_cnt+=len(edge_list[idx])
      if len(edge_list[idx]) > 1:
        check_8 = True
      edge_list[idx] = []
      while len(_edge_list)>0:
        check_edge = _edge_list[0]
        if len(edge_list[check_edge])>0:
          if len(edge_list[check_edge])>1:
            check_8 = True
          _line_cnt += len(edge_list[check_edge])
          _edge_list.extend(edge_list[check_edge])
          checked_edge_list.extend(edge_list[check_edge])
          edge_list[check_edge] = []
        
        _edge_list.remove(check_edge)
      set_checked_edge_list = set(checked_edge_list)   
      checked_edge_list = list(set_checked_edge_list) 
      if len(checked_edge_list) == _line_cnt:
        answer[1]+=1
      # elif not check_8 and len(checked_edge_list) == _line_cnt+1:
      #   answer[2]+=1
      elif check_8 and len(checked_edge_list) == _line_cnt-1:
        answer[3]+=1
      print(checked_edge_list,len(checked_edge_list),_line_cnt, answer)
      
    answer[2] -= answer[1]
    answer[2] -= answer[3]
    
    return answer

solution([[2, 3], [4, 3], [1, 1], [2, 1]]	)
solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]	)
#못품