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
    i = 0
    j = -1
    for c in combinations:
        if i % min_occur == 0:
            j += 1
        for s in c:
            bun_keys[s].append(j)
    return bun_keys

if __name__=="__main__":
    print(solution(5, 3))
    print(solution(4, 4))