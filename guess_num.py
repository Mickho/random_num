import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1 # count +=1
	
	num = input('please input number:')
	num = int(num)
	if num > r:
		print('The num is > answer')
	elif num < r:
		print('The num is < answer')
	elif num == r:
		print('Yes! You GOOD')
		break
	print('you guess', count, 'times')