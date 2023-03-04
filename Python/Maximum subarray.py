def maxSubArray(nums):
        maximum = nums[0]
        l = len(nums)
        for i in range(l):
            temp = nums[i]
            if i+1 < l:
                for j in range(i+1,l):
                    temp += nums[j]
                    if temp > maximum:
                        maximum = temp
            else:
                if nums[i] > maximum:
                    maximum = nums[i]
        return maximum

print(maxSubArray([-2,1]))
myarr = [0,1,2,3,4,5]


#https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan&id=data-structure-i