# def solution(prices):
#     answer = [0] * len(prices)
#     price_idx = []
#     for idx in range(len(prices)):
#         price_idx.append([prices[idx],idx])
        
#         i = 0
#         while i < len(price_idx):
#             if price_idx[i][1] == idx:
#                 i+=1
#                 continue
#             if price_idx[i][0]<= prices[idx] :
#                 answer[price_idx[i][1]] +=1
#                 i+=1
#             else:
#                 answer[price_idx[i][1]] +=1
#                 price_idx.pop(i)
#     print(answer)
#     return answer

# solution([1, 2, 3, 2, 3])

def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
