# 產生一個隨機整數 1~10 (不要印出來)
# 使用者可重複猜
# 猜對 印出"You are correct"
# 猜錯 提示他 比答案大/小

import random

r = random.randint(1, 100)
while True:
	x = input('please guess the number between 1-100: ')
	x = int(x)
	if x == r:
		print('You are correct')
		break
	elif x > r:
		print('lower')
	elif x < r:
		print('higher')