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
    if n <= 1:
        return 0
    while n != 1:
        if 1&n == 0:
            n = n>>1
        else:
            if n > 3 and count_tail_zeros(n+1) > count_tail_zeros(n-1):
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

a = [0]
def dp(n):
    if n <= 1:
        return 0
    for i in range(len(a),n):
        if (i+1) % 2 == 0:
            a.append(a[i>>1]+1)
        elif a[i/2] >= a[i/2-1]:
            a.append(a[i/2-1] + 2)
        else:
            a.append(a[i/2] + 2)
    return a[n-1]

def compare(n):
    for i in range(n):
        x = dp(i)
        y = solution(i)
        if x != y:
            print(i)
            print(a)
            print("%s:%s"%(x,y))
            break

if __name__=="__main__":
    #print(solution('8'))    # 2
    #print(dp(8))   # 14
    compare(100000)
