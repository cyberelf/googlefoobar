# Gearing Up for Destruction

def solution(pegs):
    """
    :type pegs: int[]
    :rtype: int[]
    """
    if len(pegs) < 2:
        return [-1, -1]
    remain = 0
    sign = -1
    for peg in pegs:
        remain += sign * peg
        sign = -sign
    remain = remain * 2 + pegs[0] + sign * pegs[-1]
    weight = -sign+2
    if remain <= 0:
        return [-1, -1]
    else:
        radius = 2*remain/weight
        for i in range(1, len(pegs)):
            radius = pegs[i]-pegs[i-1]-radius
            if radius <= 0:
                return [-1, -1]
        if remain % weight != 0:
            return [2*remain, weight]
        else:
            return [2*remain/weight, 1]

if __name__=="__main__":
    print(solution([4, 30, 50]))
    print(solution([4, 17, 50]))
