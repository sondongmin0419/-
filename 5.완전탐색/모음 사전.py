def solution(word):
    answer = 0
    m = ["A", "E", "I", "O", "U"]
    words = []
    arr = []
    for x in m:
        arr.append(x)
        words.append(("").join(arr[:]))
        for y in m:
            arr.append(y)
            words.append(("").join(arr[:]))
            for z in m:
                arr.append(z)
                words.append(("").join(arr[:]))
                for j in m:
                    arr.append(j)
                    words.append(("").join(arr[:]))
                    for l in m:
                        arr.append(l)
                        words.append(("").join(arr[:]))
                        arr.pop()
                    arr.pop()
                arr.pop()
            arr.pop()
        arr.pop()
    print(words)
    print(words.index(word))          

    answer = words.index(word) + 1
    return answer

solution("AAAE")