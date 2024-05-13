import heapq

def solution(operations):
    answer = []
    h = []
    heapq.heapify(h)
    for operation in operations:
      opt_li = operation.split()
      if (opt_li[0] == "I"):
        heapq.heappush(h,int(opt_li[1]))
      elif (opt_li[0] == "D"):
        if (len(h) == 0):
          continue
        else:
          if (opt_li[1] == "1"):
            h.pop()
          elif (opt_li[1] == "-1"):
            heapq.heappop(h)
    h.sort()
    if (len(h) == 0):
      answer = [0,0]
    else:
      answer = [h[-1],h[0]]
    print(answer)
    return answer
  
solution(["I 16","I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])