def solution(banana_list):
    """
    :type banana_list: int[]
    :rtype: int
    """

def matches(trainer_pair):
    # print all matches of a pair of trainers
    i, j = trainer_pair
    if i == j:
        return
    match_set = set()
    match_set.add((i,j))
    while i != j:
        if i > j:
            i -= j
            j <<= 1
        else:
            j -= i
            i <<= 1
        if (i,j) in match_set:
            break
        match_set.add((i,j))
        print((i,j))
    if i == j:
        print(trainer_pair)

if __name__=="__main__":
    #print(solution([1, 2, 3, 4, 5, 6]))
    # Negative conditions:
    # 1. if the sum of two numbers are not time of 4
    # Positive conditions
    # 1. if the smaller number times power of 2 equals half of the sum
    # 2. if 2 times the smaller number is larger than the large number, check condition 1 with the 
    # if 2*x>y and y>x then y-x<(x+y)/2?
    #    2y-2x<2x, x+y>2x, proven
    #for i in range(100):
    #    for j in range(100):
    #        matches((i,j))
    matches((99,77))

    