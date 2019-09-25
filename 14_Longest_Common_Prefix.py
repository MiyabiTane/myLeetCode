def longestCommonPrefix(strs):
    result=""
    i=0
    while True:
        try:
            sets=set(string[i] for string in strs)
            if len(sets)==1:
                result+=sets.pop()
                i+=1
            else:
                break
            #>>> strs=["art","bar","cat"]
            #>>> for i in range(3):
            #...     sets=set(string[i] for string in strs)
            #...     print(sets)
            #...
            #set(['a', 'c', 'b'])
            #set(['a', 'r'])
            #set(['r', 't'])
        except Exception as e:
            break

    return result
