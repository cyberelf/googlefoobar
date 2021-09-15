# Queue To Do
def solution(n):
    """
    :type n: int
    :rtype: int
    """
    # heurestics are:
    # if even, devided by 2
    # else compare tail 0's between +1 and -1, and take the longer one
    length = 0
    n = int(n)
    while n != 1:
        if 1&n == 0:
            n = n>>1
        else:
            if count_tail_zeros(n+1) >= count_tail_zeros(n-1):
                n += 1
            else:
                n -= 1
        length += 1
    return length

def count_tail_zeros(n):
    count = 0
    while 1&n == 0:
        n = n >> 1
        count += 1
    return count


if __name__=="__main__":
    print(solution('15'))    # 2
    print(solution('4'))   # 14
