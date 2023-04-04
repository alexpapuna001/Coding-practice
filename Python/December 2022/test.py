nums = [1]
target = 0
def search(nums, target):
    l = 0
    r = len(nums)-1
    if len(nums) == 1:
        if nums[0] != target:
            return -1
        else:
            return 0
    while l < r:
        m = (l+r) // 2
        if l + 1 == r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return target
            else:
                return -1
        if nums[m] != target:
            if nums[r] > target:
                l = m 
            elif nums[r] < target:
                r = m 
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
        else:
            return m
print(search(nums,target))