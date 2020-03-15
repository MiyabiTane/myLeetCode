def merge(intervals):
    if len(intervals)<2:
        return intervals
    #リストの第一引数でsortしておく。
    intervals.sort(reverse=False, key=lambda x: x[0])
    max_count=len(intervals)-1
    def sub_merge(intervals,count,max_count,pointer):
        if count==max_count:
            return intervals
        list1=intervals[pointer]
        list2=intervals[pointer+1]
        if list1[1]<list2[0]:
            return sub_merge(intervals,count+1,max_count,pointer+1)
        else:
            new_list=[list1[0],max(list1[1],list2[1])]
            intervals.pop(pointer)
            intervals.pop(pointer)
            intervals.insert(pointer,new_list)
            return sub_merge(intervals,count+1,max_count,pointer)
        
    ans=sub_merge(intervals,0,max_count,0)
    return ans

ans=merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
print(ans)



        
        