# oh no

import random
import time

primeNumbers = []
for num in range(1, 51):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				break
		else:
			primeNumbers.append(num)

while True:
	with open('./.vimrc', 'r') as f:
		x = [line.strip() for line in f]
	
	num = str(primeNumbers[random.randint(0, len(primeNumbers) - 1)])
	
	iteration = 0
	for y in x:
		if y.startswith('set tabstop'):
			tabstop = iteration
		elif y.startswith('set shiftwidth'):
			shiftwidth = iteration
		iteration += 1

	x[tabstop] = 'set tabstop=' + num
	x[shiftwidth] = 'set shiftwidth=' + num
	
	with open('./.vimrc', 'w+') as f:
		for y in x:
			f.write(y + '\n')
	
	print('tab size: ' + num)
	waitTime = random.randint(120, 600)
	print('waiting for ' + str(waitTime) + ' seconds')
	time.sleep(waitTime)
