# def sum_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# print(sum_list([1, 2, 3, 4, 5]))
# print(sum_list([10, 20, 30, 40, 50]))
# # Output: 15

# def count_even_odd(lst):
#     even_count = 0
#     odd_count = 0
#     for num in lst:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return even_count, odd_count

# print(count_even_odd([1, 2, 3, 4, 5]))
# print(count_even_odd([10, 21, 32, 43, 54]))
# # Output: (2, 3)
# # Output: (3, 2)

# def reverse_list(lst):
#     reversed_lst = []
#     for i in range(len(lst) -1, -1, -1):
#         reversed_lst.append(lst[i])
#     return reversed_lst
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list([10, 20, 30, 40, 50]))

def sum_until_even(lst):
    sum = 0
    for num in lst:
        sum += num
        # Check if the number is even
        # If it is, break the loop
        # and return the sum
        # If the number is even, break the loop
        # and return the sum
        if num % 2 == 0:
            break
    return sum

print(sum_until_even([1, 3, 5, 2, 4, 6]))  # Output: 11
print(sum_until_even([2, 4, 6, 8, 10]))  # Output: 2
print(sum_until_even([1, 3, 5, 7, 9]))  # Output: 25