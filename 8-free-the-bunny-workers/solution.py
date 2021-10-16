def solution(num_buns, num_required):
    """
    :type num_buns: int
    :type num_required: int
    :rtype: int[][]
    """
    bun_keys = []
    for i in range(num_buns):
        bun_keys.append([])
    
    combinations = []
    def combination(selected, length, cur, remain):
        if remain > length-cur:
            return
        elif remain == 0:
            combinations.append(selected)
            return
        for i in range(cur, length):
            combination(selected+[i], length, i+1, remain-1)
    # minimum ocurrance of a key
    min_occur = num_buns-num_required+1
    combination([], num_buns, 0, min_occur)
    j = 0
    for c in combinations:
        for s in c:
            bun_keys[s].append(j)
        j += 1
    return bun_keys

if __name__=="__main__":
    print(solution(5, 3))
    print(solution(4, 4))