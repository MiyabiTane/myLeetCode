def permute(nums):
    #count:[1,2,3]->[1,1,1]
    #tmp:順列ひとつひとつ
    #d:一つの順列を作り終えたか判断する
    def like_backtrack(nums,count,tmp,ans,d):
        if d==len(nums):
            copy=tmp.copy()
            ans.append(copy)
            return #ひとつ前のステップに戻る
        for i in range(len(nums)):
            if count[i]==0:
                continue
            count[i]-=1
            tmp[d]=nums[i]
            like_backtrack(nums,count,tmp,ans,d+1)
            count[i]+=1
            tmp[d]=0

    count=[1]*len(nums)
    ans=[]
    tmp=[0]*len(nums)
    like_backtrack(nums,count,tmp,ans,0)
    return ans

ans=permute([1,2,3])
print(ans)


#解説動画:https://www.youtube.com/watch?time_continue=3&v=nYFd7VHKyWQ&feature=emb_title