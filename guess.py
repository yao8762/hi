import random

r_min = int(input('請輸入最小值: '))
r_max = int(input('請輸入最大值: '))
r = random.randint(r_min, r_max)
i = 0

while True:
	i += 1
	num = int(input('請猜數字: '))
	if num == r:
		print('恭喜猜中啦')
		break
	elif num < r and num >= r_min:
		print('猜錯啦在大一點')
	elif num > r and num <= r_max:
		print('猜錯啦在小一點')
	else:
		print(f'請輸入 {r_min} 到 {r_max} 的數字!')
print(f'你一共猜了 {i} 次喔')
