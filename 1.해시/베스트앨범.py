def solution(genres, plays):
    answer = []
    gen_dic = {}
    gen_cnt_dic = {}
    for idx in range(len(genres)):
        if genres[idx] in gen_dic:
            gen_cnt_dic[genres[idx]] += plays[idx]
            gen_dic[genres[idx]].append([plays[idx],idx])
            gen_dic[genres[idx]] = sorted(gen_dic[genres[idx]], key=lambda x : [-x[0],x[1]])[0:2]
            
        else:
            gen_cnt_dic[genres[idx]] = plays[idx]
            gen_dic[genres[idx]] = [[plays[idx],idx]]
    gen_cnt_dic = sorted(gen_cnt_dic.items(), key=lambda x:x[1],reverse=True)
    for genre,cnt in gen_cnt_dic:
        for num in gen_dic[genre]:
            answer.append(num[1])
    print(gen_dic)
    print(gen_cnt_dic)
    print(answer)
    
        
    
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])