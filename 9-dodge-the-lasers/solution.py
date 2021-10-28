def solution(str_n):
    """
    :type str_n: string
    :rtype: string
    """
    pass

def solution_between(str_n):
    """Solution to this quest should be between sum(i=1..n, i) and floor(sum(i=1..n, i*sqrt(2)))
        This function returns these two numbers. 
    """
    n = int(str_n)
    m = (1+n)*n/2
    return max(int(m),int(m*(2**0.5))-n), int(m*(2**0.5))

def solution_brute(str_n):
    """Brute force solution"""
    r = 0
    for i in range(1, int(str_n)+1):
        r += int(i*(2**0.5))
    return r

if __name__=="__main__":
    print(solution_between(100))
    print(solution_brute(100))
    for i in range(1000):
        l,h = solution_between(i)
        s = solution_brute(i)
        print("{}: {}".format(i, s-l))