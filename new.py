
def get_nums(nums):
    j = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            for k in range(i, len(nums)-1):
                nums[k] = nums[k+1]
            j += 1
    return len(nums) - j














