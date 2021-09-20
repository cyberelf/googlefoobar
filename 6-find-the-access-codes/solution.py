def solution(l):
    """
    :type l: int[]
    :rtype: int
    """
    devide_counts = []
    triples = 0
    for i in range(0, len(l)):
        devide_counts.append(0)
        for j in range(i-1,-1,-1):
            if l[i] % l[j] == 0:
                devide_counts[-1] += 1
                triples += devide_counts[j]
    return triples

if __name__=="__main__":
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 2, 3, 4, 5, 10]))
    print(solution([1, 1, 1, 1]))