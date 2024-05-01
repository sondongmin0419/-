import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)  >=2:
      min_ = heapq.heappop(scoville)
      if min_ >= K:
        
        break
      else:
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_+ min_2*2)
        answer += 1
    min = heapq.heappop(scoville)
    if min < K:
      answer = -1

    return answer