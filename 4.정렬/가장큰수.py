def solution(numbers):
    answer = ''
    _numbers = list(map(str,numbers))
    _numbers = sorted(_numbers, key=lambda x :x*3 , reverse=True)
    answer = ''.join(_numbers)
    return answer

solution([3, 30, 34, 5, 9]	)
