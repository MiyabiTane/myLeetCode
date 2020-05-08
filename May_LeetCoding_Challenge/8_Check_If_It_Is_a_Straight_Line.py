import numpy as np
def checkStraightLine(coordinates) -> bool:
    if len(coordinates) == 2:
        return True
    coordinates = np.array(coordinates)
    diff_x = coordinates[1, 0] - coordinates[0, 0]
    diff_y = coordinates[1, 1] - coordinates[0, 1]
    if diff_x == 0:
        if len(set(coordinates[:, 1])) == 1:
            return True
        return False
    a = diff_y / diff_x
    b = coordinates[0,1] - a * coordinates[0,0]
    #print(diff_x, diff_y)
    for coords in coordinates[2:]:
       if coords[1] != a * coords[0] + b:
           return False
    return True


ans = checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
print(ans)
