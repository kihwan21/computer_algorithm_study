import random
import time

n = 10000

unordered = []
for i in range(0, n):
    num = random.randint(1, n)
    unordered.append(num)

#merge sort
def merge_sort(array):
    left = []
    right = []

    if len(array) <= 1:
        return array
    else:
        middle = len(array)//2
        left = array[0:middle]
        right = array[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

    #insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        new_member = array[i]
        tail_index = i-1
        while tail_index >=0 and new_member < array[tail_index]:
            array[tail_index+1] = array[tail_index]
            tail_index -= 1
        array[tail_index+1] = new_member
    return array

#시간 계산
start = time.time()
insertion_sort(unordered.copy())
end = time.time()
print("삽입정렬 시간: ", end - start)

start = time.time()
merge_sort(unordered.copy())
end = time.time()
print("병합정렬 시간: ", end - start)