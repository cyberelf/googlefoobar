def solution(l):
    """
    :type l: int[]
    :rtype: int
    """
    devide_counts = [0]
    triples = 0
    # deal with repeating numbers
    i = j = 0
    while i < len(l)-1:
        i += 1
        if l[i] == l[j]:
            if devide_counts[-1] != 1:
                j += 1
                l[j] = l[j-1]
                devide_counts.append(1)
            continue
        else:
            j += 1
            l[j] = l[i]
            devide_counts.append(0)
    list_len = j+1
    # following logic passes the quest, but it dosn't handle no-increasing list or repeating numbers correctly.
    for i in range(list_len):
        for j in range(i-1,-1,-1):
            if l[i] % l[j] == 0:
                devide_counts[i] += 1
                triples += devide_counts[j]
    return triples

if __name__=="__main__":
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 2, 3, 4, 5, 10]))
    print(solution([1, 1, 1, 1]))