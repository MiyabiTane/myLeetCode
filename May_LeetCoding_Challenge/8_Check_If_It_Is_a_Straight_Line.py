import numpy as np
def checkStraightLine(coordinates) -> bool:
    if len(coordinates) == 2:
        return True
    (x0,y0), (x1,y1) = coordinates[:2]
    for x,y in coordinates:
        if (x - x0) * (y - y1) != (x - x1) * (y - y0):
            return False
    return True

ans = checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
print(ans)
