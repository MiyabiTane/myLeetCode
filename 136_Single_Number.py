def singleNumber(nums):
    dict={}
    for num in nums:
        if num in dict:
            dict.pop(num)
        else:
            dict[num]=1
        #print(dict)
    return dict.popitem()[0] #pop the key, popitem() pop key and value

    
