import math
from decimal import Decimal, getcontext

def solution(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    solution_math_stack(str_n)

def solution_math_stack(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    # solution from https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s?newreg=cb33d186ad14497e9324f81b55236b86
    getcontext().prec = 101
    n = int(str_n)
    w = Decimal(2) ** Decimal('0.5') - 1

    def s(cur_n):
        if cur_n > 0:
            next_n = int(w*cur_n)
            mp = cur_n*next_n+cur_n*(cur_n+1)/2-next_n*(next_n+1)/2
            return mp-s(next_n)
        else:
            return 0

    return "%d" % s(n)
        

def estimation(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    # according to Weyl's equidistribution theorem, the solution is approximately equals to the middle value of min and max, i.e. m*(2**0.5)-n/2
    # Answer 2 to this question explains this in detail: https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s.
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

def count_ints(n):
    """For y=x*(2^(1/2)-1), count the number of each integer y when x equals to n. """
    w = 2**(1/2)-1
    r = [0]
    cur = 0
    for i in range(1, n+1):
        y = int(i*w)
        if y==cur:
            r[-1] += 1
        else:
            cur = y
            r.append(1)
    return r

def find_repeat():
    """Multiply 2^(1/2)-1 with natural numbers until find the smallest int, whose decimal part equal to this number"""
    w = 2**(1/2)-1
    t = w + w
    i = 2
    while w != t:
        t += w
        if t > 1:
            t -= 1
        i += 1
    return i

if __name__=="__main__":
    #print(solution_between(6))
    #print(solution_brute(6))
    #print(solution_brute_op('5'))

    # for i in range(1,10000):
    #     c = solution_brute(i)
    #     s = solution(i)
    #     if c != s:
    #         print("{} {} {}".format(i, c, s))
    print(solution_math_stack(10**100))
