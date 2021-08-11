nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]

my_list = [n * n for n in nums]

my_list = [n for n in nums if n % 2 == 0]

my_list = [(letter, n) for letter in "abcd" for n in range(4)]

# print(my_list)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

# print(list(zip(names, heros)))

my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)


my_set = {n for n in nums}
print(my_set)

# Generator expression
my_gen = (n * n for n in nums)

for n in my_gen:
    print(n)
