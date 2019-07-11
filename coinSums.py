#This solution is using recurion, which is suitable for small data like 200p
#but this is not the best optimized algorithm, please use DP for a better one
coinList = [1, 2, 5, 10, 20, 50, 100, 200]
currentDistribution = []
result = 0

def go(index):
	global currentDistribution, result
	if sum(currentDistribution) == 200:
		result += 1
	elif sum(currentDistribution) < 200:
		for i in range(coinList.index(currentDistribution[-1]), len(coinList)):
			currentDistribution.append(coinList[i])
			go(index + 1)
			currentDistribution.pop()

for coin in coinList:
	currentDistribution = [coin]
	go(1)

print(result)