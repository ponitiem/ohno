# ohno
# https://github.com/ponitiem/ohno

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
	with open('./.vimrc', 'a+') as f:
		x = [line.strip() for line in f]
	
	num = str(primeNumbers[random.randint(0, len(primeNumbers) - 1)])
	tabstop = None
	shiftwidth = None
	
	iteration = 0
	for y in x:
		if y.startswith('set tabstop'):
			tabstop = iteration
		elif y.startswith('set shiftwidth'):
			shiftwidth = iteration
		iteration += 1
	if not tabstop or not shiftwidth:
		x.append('\n')
		x.append('// created by ohno')
		if not tabstop:
			tabstop = iteration + 2
			x.append('a')
		if not shiftwidth:
			if tabstop:
				shiftwidth = iteration + 3
			else:
				shiftwidth = iteration + 2
			x.append('a') 

	x[tabstop] = 'set tabstop=' + num
	x[shiftwidth] = 'set shiftwidth=' + num
	
	with open('./.vimrc', 'w+') as f:
		for y in x:
			f.write(y + '\n')
	
	print('tab size: ' + num)
	waitTime = random.randint(120, 600)
	print('waiting for ' + str(waitTime) + ' seconds')
	time.sleep(waitTime)
