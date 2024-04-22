def solution(priorities, location):
    answer = -1
    arr = []
    cnt = 0
    for idx in range(len(priorities)):
      arr.append([priorities[idx],idx])
    priorities.sort()
    # arr_s = sorted(arr, key=lambda x : [-x[0],x[1]])
    while answer == -1:
      if arr[0][0] >= priorities[-1]:
        cnt +=1
        if arr[0][1] == location:
          answer = cnt
        
        arr.pop(0)
        priorities.pop()
      else:
        a = arr.pop(0)
        arr.append(a)
    
    print(answer)
    return answer
  
solution([2, 1, 3, 2],	2)
solution([1, 1, 9, 1, 1, 1],0)