def TwoSum(numbers,target):
    ans=[]
    for i in range(len(numbers)):
        num_want=target-numbers[i]
        if num_want in numbers and num_want!=numbers[i]:
            ans.append(i+1)
            ans.append(numbers.index(num_want)+1)
            break
        elif num_want in numbers and num_want==numbers[i]:
            if i!=len(numbers)-1:
                if num_want==numbers[i+1]:
                    ans.append(i+1)
                    ans.append(numbers.index(num_want)+2)
    return ans
