nums = [0,0,0,0]
answers = []
nums.sort()
antiduplicate = {}
count = 0
for i in range(len(nums)-2):
    count+=1
    orp1 = i+1
    p1 = i+1
    p2 = len(nums)-1 
    target = -nums[i]
    while p1 < p2:
        if nums[p1]+nums[p2] < target:
            p1+=1
        elif nums[p1]+nums[p2] > target:
            p2-=1
        elif nums[p1]+nums[p2] == target:
            if tuple([nums[i],nums[p1],nums[p2]]) not in antiduplicate:
                antiduplicate[tuple([nums[i],nums[p1],nums[p2]])] = 1
                answers.append([nums[i],nums[p1],nums[p2]])
            orp1 += 1
            p1 += 1
            p2 -= 1



print(answers)

    