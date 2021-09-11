# Solar Doomsday
import math

def solution(area):
    """
    :type area: int
    :rtype: int[]
    """
    tiles = []
    cur_area = 0
    while cur_area < area:
        area = area - cur_area
        tile = int(math.sqrt(area))
        cur_area = tile*tile
        tiles.append(cur_area)
    return tiles

if __name__=="__main__":
    print(solution(12))
    print(solution(15324))
    print(solution(999))
