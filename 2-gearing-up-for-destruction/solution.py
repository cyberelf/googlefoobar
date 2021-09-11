# Gearing Up for Destruction

def solution(pegs):
    """
    :type pegs: int[]
    :rtype: int[]
    """
    remain = 0
    sign = -1
    for peg in pegs:
        remain += sign * peg
        sign = -sign
    remain = remain * 2 + pegs[0] + sign * pegs[-1]
    weight = -sign+2
    if remain < 0 or (remain % weight != 0):
        return [-1, -1]
    else:
        return [2*remain, weight]

if __name__=="__main__":
    print(solution([4, 30, 50]))
    print(solution([4, 17, 50]))
