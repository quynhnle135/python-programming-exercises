def bubble_sort(numbers):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] >numbers[j]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers

