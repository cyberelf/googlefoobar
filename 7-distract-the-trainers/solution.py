import math 
def solution(banana_list):
    """
    :type banana_list: int[]
    :rtype: int
    """

def match_on(x, y):
    if x == y:
        return False
    g = gcd(x, y)
    x = x/g
    y = y/g
    m = min(x,y)
    n = 2
    s = x + y
    while m < s or n < s:
        m <<= 1
        n <<= 1
        if m == s or n == s:
            return False
    return True

def gcd(x, y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
  

def matches(trainer_pair):
    # print all matches of a pair of trainers
    i, j = trainer_pair
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
        #print((i,j))
    if i == j and match_on(*trainer_pair):
        print("G %s: %s" % (match_on(*trainer_pair), trainer_pair))
        #print("%d: %d" % (trainer_pair[0]+trainer_pair[1], abs(trainer_pair[0]-trainer_pair[1])))
    elif i !=j and not match_on(*trainer_pair):
        print("B %s: %s" % (match_on(*trainer_pair), trainer_pair))
        #print(match_set)

if __name__=="__main__":
    #print(solution([1, 2, 3, 4, 5, 6]))
    # Negative conditions:
    # 1. if the sum of two numbers are not time of 4
    # Positive conditions
    # 1. if the smaller number times power of 2 equals half of the sum
    # 2. if 2 times the smaller number is larger than the large number, check condition 1 with the 
    # if 2*x>y and y>x then y-x<(x+y)/2?
    #    2y-2x<2x, x+y>2x, proven
    for i in range(1<<29, (1<<29)+100):
        for j in range(1<<29, (1<<29)+100):
            #matches((i,j))
            match_on(i,j)
    #matches((99,77))

    