def solution(participant, completion):
    answer = ''
    peopleList = []
    compCheck = {}
    compNum = 0
    if len(completion) == 0:
        return participant[0]

    for comp in completion:
        if comp not in compCheck:
            compCheck[comp] = 1
        else:
            compCheck[comp] += 1
    for part in participant:
        if part not in compCheck:
            answer = part
            break
            return part
        elif compCheck[part] == 0:
            answer = part
            break
            return part
        else:
            compCheck[part] -= 1
    print(answer)
    return answer


solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
