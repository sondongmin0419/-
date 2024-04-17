def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0])
    for num in arr:
      if answer[-1] != num:
        answer.append(num)
      
    print(answer)
    return answer
  
solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])