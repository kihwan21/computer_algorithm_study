# 주어진 틀 삭제 금지
def construct_max_heap(array):
    if array[3] < array[5]:
        array[3], array[5] = array[5], array[3]
    if array[2] < array[4]:
        array[2], array[4] = array[4], array[2]
    if array[1] < array[3]:
        array[1], array[3] = array[3], array[1] 
    if array[0] < array[2]:
        array[0], array[2] = array[2], array[0]
    if array[0] < array[1]:
        array[0], array[1] = array[1], array[0]



def delete_max_heap(array):
    for i in array:
        last_index = i  # 루트가 인덱스 뒤로 오게 함
        print(last_index)

array = [12, 11, 13, 5, 6, 7]
print('Original: ' + str(array))

construct_max_heap(array)
print('Max heap: ' + str(array))

delete_max_heap(array)
print('Result: ' + str(array))
