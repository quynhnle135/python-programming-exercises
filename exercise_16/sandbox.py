nums = [1, 2, 1, 3, 2, 2, 4, 5]
nums_dict = {}
for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 1
        # print(f"{num}: {nums_dict[num]}")
    else:
        nums_dict[num] += 1
        # print(f"{num}: {nums_dict[num]}")

print(nums_dict)
# print keys
for key in nums_dict:
    print(key, end=" ")

print()
# print values
for value in nums_dict.values():
    print(value, end=" ")

print()
# print values with key
for key in nums_dict:
    print(nums_dict[key], end=" ")

maxCount = 0
greatestKey = 0
for key in nums_dict:
    if nums_dict[key] > maxCount:
        maxCount = nums_dict[key]
        greatestKey = key
print()
print(f"Greatest Key: {greatestKey}")
print(f"maxCount: {maxCount}")