def find_median(nums):
    if not nums:
        return None
    nums.sort()
    if len(nums) % 2 == 1:
        return nums[len(nums) // 2]

    if len(nums) % 2 == 0:
        return round((nums[(len(nums) // 2) - 1] + nums[(len(nums) // 2)]) / 2, 2)
