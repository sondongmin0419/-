def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx in range(len(phone_book)-1):
      if phone_book[idx+1].find(phone_book[idx]) == 0:
        answer=False
        break
    return answer
  
solution(["119", "97674223", "1195524421"]	)
solution(["123","456","789"]	)
solution(["12","123","1235","567","88"]	)