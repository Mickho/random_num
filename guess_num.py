import random

r = random.randint(1, 100)
while True:
	num = input('please input number:')
	num = int(num)
	if num > r:
		print('The num is > answer')
	elif num < r:
		print('The num is < answer')
	elif num == r:
		print('Yes! You GOOD')
		break