
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(f'檔案讀取完畢，總共有{len(data)}筆資料')

totle = 0
for d in data:
	totle += len(d)
print(f'留言的平均長度為: {totle/len(data)}')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(f'總共有 {len(new)} 筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(f'總共有 {len(good)} 筆留言有包含"good"')
print(good[0])

