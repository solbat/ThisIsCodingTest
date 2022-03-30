# selection sort

array = list(map(int, input().split()))

for i in range(len(array)):
    min_index = 1
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# insertion sort

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

# quick sort
def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left += 1
        while right>start and array[right]>=array[pivot]:
            right -= 1
        if left>right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

def quick_sort_good(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_good(left_side) + [pivot] + quick_sort_good(right_side)

