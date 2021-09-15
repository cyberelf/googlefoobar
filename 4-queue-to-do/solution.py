# Queue To Do
def solution(start, length):
    """
    :type start: int
    :type length: int
    :rtype: int
    """
    MAX_ID = 2000000000
    rslt = 0
    cur_length = length
    while cur_length > 0 and start < MAX_ID:
        if start+cur_length-1 <= MAX_ID:
            rslt ^= fast_xor(start, start+cur_length-1)
        else:
            rslt ^= fast_xor(start, MAX_ID)
        start += length
        cur_length -= 1
    return rslt

def fast_xor(a, b):
    # b is greater than a
    rslt = 0
    if a == 0:
        a = 1
    if (b-a) < 4:
        for i in range(a,b+1):
            rslt ^= i
        return rslt
    else:
        # xor head
        for i in range(a-1-(a-1)%4, a):
            rslt ^= i
        # xor tail
        for i in range(b-b%4, b+1):
            rslt ^= i
        return rslt

def common_xor(a,b):
    rslt = 0
    for i in range(a,b+1):
        rslt ^= i
    return rslt

if __name__=="__main__":
    print(solution(0,3))    # 2
    print(solution(17,4))   # 14
    print(solution(0,2000000)) # 23552
    print(common_xor(0,200))