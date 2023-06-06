# practice index()
my_text = "hello, world"
print(my_text.index('e'))
print(my_text.index('l'))
# print(my_text.index('!'))

# word_1 = "one"
# word_2 = "two"
# word_3 = "three"
# my_text = word_1 + my_text
# print(my_text)
my_number = "123456789"

# practice range in for loop, print the list backward
for i in range(len(my_number) - 1, -1, -1):
    print(my_number[i], end=" ")
print()

# print the list backward and skip one element each time
for i in range(len(my_number) - 1, -1, -2):
    print(my_number[i], end=" ")
print()

# cut the last element of the string
print(my_text[:-1])