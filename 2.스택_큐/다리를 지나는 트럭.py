def solution(bridge_length, weight, truck_weights):
    answer = 0
    pass_truck_cnt = 0
    passing_trurck_arr = []
    passing_trurck_bridge_arr = []
    truck_num = len(truck_weights)
    while pass_truck_cnt < truck_num:
        if len(truck_weights) == 0:
            answer += (bridge_length - passing_trurck_bridge_arr[-1] + 1)
            pass_truck_cnt += len(passing_trurck_bridge_arr)
            break
        answer += 1
        if sum(passing_trurck_arr)+truck_weights[0] <= weight:
            passing_trurck_arr.append(truck_weights.pop(0))
            passing_trurck_bridge_arr.append(0)
        for idx in range(len(passing_trurck_bridge_arr)):
            passing_trurck_bridge_arr[idx] += 1
        if passing_trurck_bridge_arr[0] == bridge_length:
            passing_trurck_bridge_arr.pop(0)
            passing_trurck_arr.pop(0)
            pass_truck_cnt += 1

    print(answer)
    return answer


solution(2,	10,	[7, 4, 5, 6])
solution(100, 100,	[10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
