def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1_cnt = 0
    p2_cnt = 0
    p3_cnt = 0
    answer = []
    for idx in range(len(answers)):
        if (p1[idx % 5] == answers[idx]):
            p1_cnt += 1
        if (p2[idx % 8] == answers[idx]):
            p2_cnt += 1
        if (p3[idx % 10] == answers[idx]):
            p3_cnt += 1

    p_cnts = [[p1_cnt, 1], [p2_cnt, 2], [p3_cnt, 3]]
    p_cnts = sorted(p_cnts, key=lambda x: [x[0], -x[1]], reverse=True)
    max_cnt = max(p1_cnt,p2_cnt,p3_cnt)
    for p_cnt in p_cnts:
        if p_cnt[0] == max_cnt:
            answer.append(p_cnt[1])
    print(answer)
    return answer


solution([1, 2, 3, 4, 5])
