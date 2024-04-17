def solution(edges):
    answer = [0,0,0,0]
    graph_list = []
    find_edge = 0
    edge_list = []
    print(edges)
    edges.sort()
    print(edges)
    for edge in edges:
      print(edge)
      find = 0
      # if find_edge == 0:
      #   if edge[0] not in edge_list:
      #     edge_list.append(edge[0])
      #   else:
      #     find_edge = edge[0]
          
      for i in range(len(graph_list)):
        if graph_list[i][-1] == edge[0]:
          graph_list[i].append(edge[1])
          find += 1
          break
        elif graph_list[i][0] == edge[1]:
          graph_list[i].insert(0,edge[0])
          find += 1
          break

      if find == 0:
        graph_list.append(edge)
              print(graph_list)  
    
    # print(edge_list)
    # print(find_edge)
    print(graph_list)
    # answer.append(find_edge)
    # for graph in graph_list:
    #   if graph[0] == find_edge:
    #     continue
    #   if graph[0]:
        
    
    return answer
  
  
solution([[2, 3], [4, 3], [1, 1], [2, 1]]	)
solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]	)
# 못품