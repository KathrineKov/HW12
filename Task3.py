def custom_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

short_list = [5, 2, 9, 1, 5]
long_list = [10, 3, 6, 2, 5, 9, 8, 4, 7, 1]

print("Sorted short list:", custom_sort(short_list))
print("Sorted long list:", custom_sort(long_list))