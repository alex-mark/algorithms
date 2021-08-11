from typing import Iterator


def square_numbers(nums: list[int]) -> list[int]:
    result = []
    for i in nums:
        result.append(i * i)
    return result


def square_numbers_gen(nums: list[int]) -> Iterator[int]:
    for i in nums:
        yield i * i


# my_nums = square_numbers_gen([1, 2, 3, 4, 5])

# Generator expression
# returns iterator
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))  # Raises StopIteration

for num in my_nums:
    print(num)
