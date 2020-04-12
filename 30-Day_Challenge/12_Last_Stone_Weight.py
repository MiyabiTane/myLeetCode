def lastStoneWeight(stones):
    if len(stones)==0:
        return 0
    if len(stones)==1:
        return stones[0]
    stones.sort()
    #print(stones)

    stone1 = stones.pop()
    stone2 = stones.pop()

    if stone1 != stone2:
        stones.append(stone1-stone2)
    
    return lastStoneWeight(stones)

ans = lastStoneWeight([2,7,4,1,8,1])
print(ans)
    