# numbers = {'1':2, '2':3, '3':4, '4':5}
# print(numbers)
# print(numbers['2'])

# for number in numbers:
# 	print(int(numbers[number]) + 'が好きです！')

int_list = [1, 2, 3]
num_list = list(map(str, int_list))
print(num_list)

str_list = ["1", "2", "3"]
num_list = list(map(int, str_list))
print(num_list)

str_list = ["1.1", "2", "3"]
num_list = list(map(float, str_list))
print(num_list)

def func(n):
	return n ** 2
	
a = [1, 2, 3, 4]
num = list(map(func, a))
print(num)