

data = []
count = 0
words_count = {}


def main():
	file = 'reviews.txt'
	data = read_file(file, count)
	words_count = words(data)
	search(words_count)
	print('感謝使用本查詢功能')


def read_file(file, count):
	with open(file, 'r') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 5000 == 0:
				print(len(data))
	print(f'檔案讀取完畢，總共有{len(data)}筆資料')
	return data


def words(data):
	print('正在計算單字數量，請稍後...')
	for d in data:
		words = d.split()
		for word in words:
			if word not in words_count:
				words_count[word] = 1
			else:
				words_count[word] += 1

	# for word in words_count:
	# 	if words_count[word] > 10000:
	# 		print(word, words_count[word])
	print(f'一共有: {len(words_count)} 個單字')
	return words_count

def search(words_count):
	while True:
		word = input('請問你想查什麼字: ')
		if word == 'q' or word == 'exit':
			break
		elif word in words_count:
			print(word, '出現過的次數為: ', words_count[word])
		else:
			print(word, '沒有出現過')

if __name__ == '__main__':
	main()











# totle = 0
# for d in data:
# 	totle += len(d)
# print(f'留言的平均長度為: {totle/len(data)}')

# # new = []
# # for d in data:
# # 	if len(d) < 100:
# # 		new.append(d)
# new = [d for d in data if len(d) < 100]
# print(f'總共有 {len(new)} 筆留言長度小於100')

# # good = []
# # for d in data:
# # 	if 'good' in d:
# # 		good.append(d)
# good = [d for d in data if 'good' in d]
# print(f'總共有 {len(good)} 筆留言提到"good"')
