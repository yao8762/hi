data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

totle = 0
for d in data:
	totle += len(d)

print(f'檔案讀取完畢，總共有{len(data)}筆資料, 留言的平均長度為: {totle/len(data)}')

new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print(f'總共有 {len(new)} 比留言長度小於100')
print(new[0])
