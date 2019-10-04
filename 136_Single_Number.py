def singleNumber(nums):
    dict={}
    for num in nums:
        if num in dict:
            dict.pop(num)
        else:
            dict[num]=1
        #print(dict)
    return dict.popitem()[0] #pop the key, popitem() pop key and value

    """al_ex_num=[]
    for num in nums:
        if num in al_ex_num:
            al_ex_num.pop(al_ex_num.index(num))
        else:
            al_ex_num.append(num)
    return al_ex_num.pop(0)"""
