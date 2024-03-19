list_nums = [1,2,3,4]

# def square_num(list_nums):
#     for x in list_nums:
#         yield x * x

# generated = square_num(list_nums)
# print(next(generated))
# print(next(generated))
# print(list(generated))

# ///////////create a new generator//////////////////
new_generator = (x*x for x in list_nums)
print(list(new_generator))

list_iter = iter(list_nums)
print(next(list_iter))
print(next(list_iter))

