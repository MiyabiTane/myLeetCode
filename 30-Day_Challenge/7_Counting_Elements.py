def countElements(arr):
    ans = 0
    for num in arr:
        if num+1 in arr:
            ans+=1
    return ans 


ans = countElements([1, 3, 2, 3, 5, 0])
print(ans)
