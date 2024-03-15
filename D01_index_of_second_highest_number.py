# return the index of second highest number
def second_highest_no(arr):
    second_highest_number = 0
    highest = min(arr)
    for i in range(len(arr)):
        if arr[i] > highest:
            second_highest_number = highest
            highest = arr[i]
        else:
            second_highest_number=max(arr[i], second_highest_number)
    index = arr.index(second_highest_number)
    return index


print(second_highest_no([10, 2, 56, 7, 9]))
