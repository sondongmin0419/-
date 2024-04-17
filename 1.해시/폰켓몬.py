def solution(nums):
    answer = 0
    numList = []
    selectNum = len(nums)//2
    for num in nums:
      if num not in numList:
        numList.append(num)
    if len(numList) > selectNum:
      answer = selectNum
    else:
      answer = len(numList)
      
    print(answer)
    return answer
  
solution([3,1,2,3])