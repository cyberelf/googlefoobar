# Queue To Do
def solution(start, length):
    """
    :type start: int
    :type length: int
    :rtype: int
    """
    rslt = 0
    cur_length = length
    for l in range(length):
        for i in range(length):
            if i < cur_length:
                rslt ^= start
            start += 1
        cur_length -= 1
    return rslt

if __name__=="__main__":
    print(solution(0,3))
    print(solution(17,4))
    print(solution(100,2))