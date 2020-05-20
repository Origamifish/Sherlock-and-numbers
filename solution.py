testCases = int(input())
for i in range(testCases):
	a = []
	info = input().split()
	
	for i in range(len(info)):
		info[i] = int(info[i])

	p = info[2]
	n = info[0]
	k = info[1]
	removedNums = list(map(int, input().split(" ")))
	removedNums.sort()
	for i in range(len(removedNums)):
		if removedNums[i] <= p:
			p += 1
			n -= 1
		elif removedNums[i] > p:
			n -= 1 
		
	if info[2] <= n:
		print(p)
	else:
		print(-1)

