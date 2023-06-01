def find_average(nums):
    count = 0
    sum = 0
    for num in nums:
        count += 1
        sum += num
    return round(sum / count, 2)
