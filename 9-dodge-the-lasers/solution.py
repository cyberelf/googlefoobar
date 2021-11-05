import math 

def solution(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    n = float(str_n)
    m = (1+n)*n/2
    return m*(2**0.5)-n/2

def estimation(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    # according to Weyl's equidistribution theorem, the solution is approximately equals to the middle value of min and max, i.e. m*(2**0.5)-n/2
    n = float(str_n)
    m = (1+n)*n/2
    return m*(2**0.5)-n/2

def solution_between(str_n):
    """Solution to this quest should be between sum(i=1..n, i) and floor(sum(i=1..n, i*sqrt(2)))
        This function returns these two numbers. 
    """
    n = int(str_n)
    m = (1+n)*n/2
    # 2^(1/2) is a bit less than 1.5, so use 1.5 as its' uppper limit
    # min=m*(2^0.5)-n
    # max=m*(2^0.5)
    p5m = m*1.5 - 0.5 * math.ceil(n/2)
    return max(int(m),int(m*(2**0.5))-n), min(int(m*(2**0.5)), p5m)

def solution_brute(str_n):
    """Brute force solution
    The result is not accurate when n is larger than 10^6, perhaps because the resolutioin of the int size. 1+23 bits of int part
    and 40 bits of double decimal part of a double number will overflow when it's too big.
    """
    r = 0
    s = 2**0.5
    l = 0
    for i in range(1, int(str_n)+1):
        l += s
        r += int(l)
    return r

def solution_brute_op(str_n):
    """Brute force solution"""
    d = 0
    n = int(str_n)
    m = (1+n)*n/2
    r = 2**0.5-1
    rm = 0
    for i in range(1, n+1):
        rm += r
        if rm >= 1:
            rm = rm-1
        d += rm
    return int(m*(2**0.5)-d)

if __name__=="__main__":
    #print(solution_between(6))
    #print(solution_brute(6))
    #print(solution_brute_op('5'))

    for i in range(1,1001):
        c = solution_brute_op(i)
        s = solution(i)
        if c != round(s):
            print("{} {} {}".format(i, c, s))
