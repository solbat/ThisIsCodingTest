def solution(arr):
    answer = []

    data = [0] * 101
    for val in arr:
        data[val] += 1

    for val in arr:
        if data[val] > 1:
            answer.append(data[val])
            data[val] = 0
    
    if len(answer) == 0:
        return -1
    else:
        return answer

arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
arr = [3, 5, 7, 9, 1]

print(solution(arr))