def solution(k, dungeons):
    answer = [-1]
    dungeons = sorted(dungeons, key=lambda x: [x[0], -x[1]], reverse=True)
    a_k = k
    dun_cnt = 0
    len_dungeons = len(dungeons)
    check_dungeons = [False] * len_dungeons
    print(dungeons)

    def roof(a_k, dun_cnt):
        for i in range(len_dungeons):
            if check_dungeons[i] == False and a_k >= dungeons[i][0] and a_k >= dungeons[i][1]:
                check_dungeons[i] = True
                a_k -= dungeons[i][1]
                dun_cnt += 1
                roof(a_k, dun_cnt)
                a_k += dungeons[i][1]
                check_dungeons[i] = False
                dun_cnt -= 1
        if answer[0] < dun_cnt:
            answer[0] = dun_cnt
        print(answer[0])

    roof(a_k, dun_cnt)
    print(answer[0])
    return answer[0]


solution(80, [[80, 20], [50, 40], [30, 10]])
