def solution(s):
    answer = True
    l_cnt = 0
    r_cnt = 0
    for x in s:
      if x == "(":
        l_cnt+=1
      elif x == ")":
        r_cnt+=1
      if r_cnt>l_cnt:
        answer = False
    if l_cnt != r_cnt:
      answer = False
    print(answer)
    return answer
  
solution(")()(")