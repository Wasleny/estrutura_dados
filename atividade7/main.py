def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)


def partition(arr, left, right):
    pivot = arr[right][0]
    i = left - 1
    for j in range(left, right):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def two_sum_quick_sort(nums, target):
    enumerated_nums = [(num, idx) for idx, num in enumerate(nums)]

    quick_sort(enumerated_nums, 0, len(enumerated_nums) - 1)

    left, right = 0, len(enumerated_nums) - 1
    while left < right:
        soma = enumerated_nums[left][0] + enumerated_nums[right][0]
        if soma == target:
            return [enumerated_nums[left][1], enumerated_nums[right][1]]
        elif soma < target:
            left += 1
        else:
            right -= 1


def two_sum_hash(nums, target):
    value_to_index = {}

    for i, current_value in enumerate(nums):
        complement = target - current_value

        if complement in value_to_index:
            return [value_to_index[complement], i]

        value_to_index[current_value] = i


print(two_sum_brute_force([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_brute_force([3, 2, 4], 6))  # [1, 2]
print(two_sum_brute_force([3, 3], 6))  # [0, 1]

print(two_sum_quick_sort([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_quick_sort([3, 2, 4], 6))  # [1, 2]
print(two_sum_quick_sort([3, 3], 6))  # [0, 1]

print(two_sum_hash([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_hash([3, 2, 4], 6))  # [1, 2]
print(two_sum_hash([3, 3], 6))  # [0, 1]
