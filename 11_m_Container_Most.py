def maxArea(height):
    start=0
    end=len(height)-1
    max_area=[0]
    while start<end:
        if (end-start)*min(height[start],height[end])>max_area[-1]:
            max_area.append((end-start)*min(height[start],height[end]))
        if height[start]>=height[end]:
            end-=1
        elif height[start]<height[end]:
            start+=1
        #print("start,end,max_area = {},{},{}".format(start,end,max_area))
    return max(max_area)
