def find_smallest(nums):
    if not nums:
        return None

    smallest = 100000

    for num in nums:
        if num < smallest:
            smallest = num

    return smallest


def find_biggest(nums):
    if not nums:
        return None

    biggest = -100000

    for num in nums:
        if num > biggest:
            biggest = num

    return biggest


