import heapq


def solution(jobs):
    answer = 0
    cnt = len(jobs)
    w_cnt = 0
    time = 0
    time_sum = 0
    working_jobs = []
    wait_jobs = []
    heapq.heapify(wait_jobs)
    heapq.heapify(jobs)
    while w_cnt < cnt:
        if working_jobs:
            if jobs and jobs[0][0] <= time:
                job = heapq.heappop(jobs)
                heapq.heappush(wait_jobs, [job[1], job[0]])
            else:
                working_jobs = []
                w_cnt += 1
        else:
            if wait_jobs:
                working_jobs = heapq.heappop(wait_jobs)
                time += working_jobs[0]
                time_sum += (time-working_jobs[1])
            else:
                job = heapq.heappop(jobs)
                working_jobs = [job[1], job[0]]
                temp_time = time
                time = working_jobs[0] + working_jobs[1]
                time_sum += working_jobs[0]

    print(time_sum)
    print(time_sum//cnt)
    answer = time_sum//cnt

    return answer

solution([[0, 10], [4, 10], [5, 11], [15, 2]])
