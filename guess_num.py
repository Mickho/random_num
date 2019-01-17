import random
start = input('please input start num:')
end = input('please input end num:')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
		print('you guess', count, 'times') #為了在猜中最後一次的計數
		break
	print('you guess', count, 'times')