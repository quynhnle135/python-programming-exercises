import random

lowercase = "abcedfghijklmnopqrsatuvwxyz"
random_str = []
for i in range(11):
    random_str.append(lowercase[random.randint(0, 25)])

print("".join(random_str))

my_list = ["1", "2", "3", "4"]
print("-".join(my_list))
