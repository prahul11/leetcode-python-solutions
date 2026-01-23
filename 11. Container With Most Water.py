height = [1,8,6,2,5,4,8,3,7]
target = 49


def max_water(height):
    area = 0

    l=0
    r=len(height)-1
    while l < r:
        print(r-l, l, r)
        area = max(((r-l) * min(height[l], height[r])), area)
        print(area)
        if height[l] < height[r] :
            print("left chhota")
            l+=1
        else:
            print("right chhota")
            r-=1
    return area

print( max_water([8,7,2,1]))




 