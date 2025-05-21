# 這是一個猜數字遊戲　使用random
import random
no = random.randint(1, 100)
print("這是一個猜數字遊戲，請你從1到100中間猜一個數字，我會告訴你正確，或是太大，或是太小")
while True:
	answer = int(input("請輸入你的猜想？"))
	if answer == no:
		result -= 1
		print("你答對了！")
		break
	elif answer > no:
		print("你猜的數字太大了！")
	elif answer < no:
		print("你猜的數字太小了！")
