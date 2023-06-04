my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
duplicated_list = [0] * len(my_list)
print(duplicated_list)

index = 0
for number in my_list:
    duplicated_list[index] = number * 2
    index += 1

print(duplicated_list)

copy_list = []
for number in my_list:
    copy_list.append(number)

# practice print 2D list
my_matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for row in my_matrix:
    print(row)