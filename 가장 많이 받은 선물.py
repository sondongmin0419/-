def solution(friends, gifts):
    answer = 0
    print(friends)
    print(gifts)
    friends_length = len(friends)
    count_gifts = [[0 for i in range(friends_length)]
                   for j in range(friends_length)]
    gifts_score = [0]*friends_length
    receive_gift_count = [0]*friends_length
    max_receive_gift_count = 0
    
    for gift in gifts:
        gift_from_to = gift.split(" ")
        from_idx = friends.index(gift_from_to[0])
        to_idx = friends.index(gift_from_to[1])
        count_gifts[from_idx][to_idx] += 1
    
    for i in range(friends_length):
        for j in range(friends_length):
            gifts_score[i] += count_gifts[i][j]
            gifts_score[i] -= count_gifts[j][i]
    
    for i in range(friends_length):
        for j in range(i,friends_length):
            if i==j:
                continue
            if count_gifts[i][j]>count_gifts[j][i]:
                receive_gift_count[i]+=1
            elif count_gifts[i][j] == count_gifts[j][i]:
                if gifts_score[i]>gifts_score[j]:
                    receive_gift_count[i]+=1
                elif gifts_score[i]<gifts_score[j]:
                    receive_gift_count[j]+=1
            elif count_gifts[i][j] < count_gifts[j][i]:
                receive_gift_count[j]+=1
            if max_receive_gift_count < receive_gift_count[i]:
                max_receive_gift_count = receive_gift_count[i]
            if max_receive_gift_count < receive_gift_count[j]:
                max_receive_gift_count = receive_gift_count[j]     
    
    return max_receive_gift_count


solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo",
         "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
