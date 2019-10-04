def singleNumber(nums):
    al_ex_num=[]
    for num in nums:
        if num in al_ex_num:
            al_ex_num.pop(al_ex_num.index(num))
        else:
            al_ex_num.append(num)
    return al_ex_num.pop(0)
