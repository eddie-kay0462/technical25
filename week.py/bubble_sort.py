def bubble_sort(list):
    unsorted_until_index = len(list) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index-=1
    return list



print(bubble_sort([3, 2, 5, 4, 1, 11]))