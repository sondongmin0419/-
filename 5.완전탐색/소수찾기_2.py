def solution(numbers):
    def dfs(c_num):
        if c_num:
            result.append(int(c_num))
        if sum(visited) == len(visited):
            return

        for i in range(len(n_list)):
            if visited[i]==1:
                continue
            else:
                c_num += n_list[i]
                visited[i] = 1
                dfs(c_num)
                c_num = c_num[:len(c_num)-1]
                visited[i] = 0
        return

    answer = 0
    n_list = list(numbers)
    n_list.sort(reverse=True)
    max_number = int(''.join(n_list))
    s_num = [True] * (max_number+1)
    s_num[0] = False
    s_num[1] =False
    for i in range(2,(max_number+1)):
        if s_num[i] == True:
            t = 2
            while i*t<(max_number+1):
                s_num[i*t] = False
                t+=1
    result = []
    c_num = ''
    visited = [0]*len(n_list)
    dfs(c_num)
    print(result)
    result = list(set(result))
    # print(result)
    # print(max_number)
    # print(s_num)
    for i in result:
        if s_num[i]:
            answer+=1
    return answer
  
solution("011")