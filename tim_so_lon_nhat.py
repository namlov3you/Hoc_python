nums = [12, 45, 7, 89, 32, 54]
num_max = nums[0]
for i in range(len(nums)):
    if nums[i] > num_max:
        num_max = nums[i]

print("num max = ", num_max)