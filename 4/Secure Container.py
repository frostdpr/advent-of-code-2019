### PART 1 ###
def monotonic_and_adj(num):
	adj_flag = False
	num = str(num)
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
		if num[i] == num[i+1]:
			adj_flag = True
	return True and adj_flag


### PART 2 ###
def monotonic_and_adj_modified(num):
	adj_flag = False
	adj_cur = ''
	num = str(num)
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
		if adj_flag and num[i] != adj_cur:
			continue
		if num[i] == num[i+1] and num[i] == adj_cur:
			adj_flag = False
		elif num[i] == num[i+1]:
			adj_cur = num[i]
			adj_flag = True

	return True and adj_flag

num_valid = 0

print(monotonic_and_adj_modified(112233))
print(monotonic_and_adj_modified(123444))
print(monotonic_and_adj_modified(112222))

for i in range(136818, 685980):
	if monotonic_and_adj_modified(i):
		num_valid+=1

print(num_valid)
