# 產生一個隨機整數 1~100 (不要印出來)
# 使用者可重複猜
# 猜對 印出"You are correct"
# 猜錯 提示他 比答案大/小

import random

a = input('start in: ')
b = input('End in: ')
a = int(a)
b = int(b)
r = random.randint(a, b)
count = 0
while True:
	count += 1 # count = count + 1
	x = input('please guess the number: ')
	x = int(x)
	if x == r:
		print('You are correct')
		print ('This is the', count, 'time(s)')
		break
	elif x > r:
		print('lower')
	elif x < r:
		print('higher')
	print ('This is the', count, 'time(s)')