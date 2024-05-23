def solution(citations):
    answer = 0
    citations = sorted(citations,reverse=True)
    c_len = len(citations)
    for idx in range(c_len):
        if idx+1 <= citations[idx]:
            answer = idx+1
        if citations[idx] <= idx+1:
            return max(citations[idx],answer)
            
    return answer

solution([3, 0, 6, 3, 5]	)