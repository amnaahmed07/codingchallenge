# # return the index of second highest number
# def second_highest_no(arr):
#     second_highest_number = 0
#     highest = min(arr)
#     for i in range(len(arr)):
#         if arr[i] > highest:
#             second_highest_number = highest
#             highest = arr[i]
#         else:
#             second_highest_number=max(arr[i], second_highest_number)
#     index = arr.index(second_highest_number)
#     return index
#
#
# print(second_highest_no([10, 2, 56, 7, 9]))

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#  You can return the answer in any order.
def two_sum(i_list, target):
    sum = 0
    n = len(i_list)
    for i in range(n):
        for j in range(i + 1, n):
            if i_list[i] + i_list[j] == target:
                return i, j

    return None

l = [3, 3, 6, 7, 5]
target = 13
print(two_sum(l, target))