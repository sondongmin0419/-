def DFS(v, graph, visited, check_link):
    cnt = 1
    
    visited[v] = True
    
    for adj_v in graph[v]:
        if visited[adj_v] == False and check_link[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check_link)
            
    return cnt


def solution(n, wires):
    answer = 1e9
    check_link = [[True]*(n+1) for _ in range(n+1)]
    
    graph = [[] for _ in range(n+1)]
    cnt_all = []
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in wires:
        visited = [False] * (n+1)
        
        check_link[a][b] = False
        cnt_a = DFS(a, graph, visited, check_link)
        cnt_b = DFS(b, graph, visited, check_link)
        check_link[a][b] = True
        
        answer = min(answer, abs(cnt_a - cnt_b))    
    return answer


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
