result = 2
nums = [1, 2]

while nums[-1] <= 4000000:
	nums.append(nums[-1] + nums[-2])
	if nums[-1] % 2 == 0:
		result += nums[-1]

print(result)