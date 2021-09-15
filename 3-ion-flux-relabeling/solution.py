# Ion Flux Relabeling
def solution(h, q):
    """
    :type h: int
    :type q: int[]
    :rtype: int[]
    """
    max_node = 2**h
    tree = [0] * max_node
    ptree = [0] * max_node
    cur_node = 1
    stack = [cur_node]
    order = 0
    while len(stack) > 0:
        cur_node = stack[-1]
        left = cur_node*2
        if left >= max_node:
            # leaf
            stack.pop()
            tree[cur_node] = order
            order += 1
        elif tree[left] == 0:
            # left child not visited
            stack.append(left)
        elif tree[left+1] == 0:
            stack.append(left+1)
        else:
            stack.pop()
            tree[cur_node] = order
            ptree[tree[left]] = ptree[tree[left+1]] = order
            order += 1
    rslt = []
    for c in q:
        if c < max_node - 2 and c > 0:
            rslt.append(ptree[c])
        else:
            rslt.append(-1)
    return rslt

if __name__=="__main__":
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))