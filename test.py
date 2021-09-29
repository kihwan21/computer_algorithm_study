#내림차순으로 나와서 그렇지 값은 출력이됨

# array = [64, 25, 12, 22, 11]

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         new_member = array[i]
#         j = i
#         while j >= 0 and new_member > array[j - 1]:
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = new_member
#     return array

# insertion_sort(array)
# print(array)

# test_arr = [64, 25, 12, 22, 11]

# def insertion_sort(arr):
#     for i in range(len(arr)): 
#         num_we_are_on = arr[i]
#         j = i - 1 
#         while j >= 0 and arr[j] > num_we_are_on:
#                 arr[j+1] = arr[j]
#                 j -= 1
#         j += 1
#         arr[j] = num_we_are_on
#     return arr


# ordered_array = insertion_sort(test_arr)
# print(ordered_array)

unordered = [64, 25, 12, 22, 11]

def insertion_sort(arr):
    for i in range(len(arr)): 
        num_we_are_on = arr[i]
        j = i - 1 
        while j >= 0 and arr[j] > num_we_are_on:
                arr[j+1] = arr[j]
                j -= 1
        j += 1
        arr[j] = num_we_are_on
    return arr

insertion_sort(unordered)

ordered_array = insertion_sort(unordered)
print(ordered_array)