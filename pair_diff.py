def pair_diff(nums,k):
    pairs = []
    #If k == 0, calculate the counts of numbers, and return pairs where count > 1
    if k == 0:
        count_dict = {}
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        for key in count_dict.keys():
            if count_dict[key] > 1:
                pairs.append((key,key))
        return pairs
    #if count is not 0, check if num+k in list  
    for num in nums:
        if num+k in nums:
            pairs.append((num,num+k))
    return list(set(pairs))

print(pair_diff(nums = [1,3,5], k = 2))  