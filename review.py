data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('档案读取完了,', '总共有', len(data), '条review')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('review的平均长度为:', sum_len / len(data))

new = []
for d in data:
	if len(d) <= 100:
		new.append(d)
print('留言长度小于100的一共有', len(new), '条')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言里面有good的有', len(good), '条')
print(good[0])
print(good[1])