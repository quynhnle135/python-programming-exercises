def find_mode(nums):
    if not nums:
        return None

    maxCount = 0
    mode = 0
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    for num in nums_dict:
        if nums_dict[num] > maxCount:
            maxCount = nums_dict[num]
            mode = num
    return mode