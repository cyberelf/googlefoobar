from collections import defaultdict

# This is not a correct answer, but may provide some faster solution.
def solution(states):
    true_states = (1, 2, 4, 8)
    false_states = (0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15)
    possible_states = {True: true_states, False: false_states}

    # start from lower right corner
    x = len(states)-1
    y = len(states[0])-1
    count = 0
    solution_stacks = []
    for _ in range(x+1):
        stacks = []
        for _ in range(y+1):
            stacks.append([])
        solution_stacks.append(stacks)
    if states[x][y] == True:
        solution_stacks[x][y] = list(true_states)
    else:
        solution_stacks[x][y] = list(false_states)

    # counts of the previous row
    pre_counts = [{i: 1 for i in range(16)} for _ in range(len(states[0]))]
    for i in range(x, -1, -1):
        cur_counts = [defaultdict(int) for _ in range(len(states[0]))]
        for j in range(y, -1, -1):
            cur_state = states[i][j]
            if i == x and j == y:
                for s in possible_states[cur_state]:
                    cur_counts[j][s] = 1
            elif i == x:
                # right
                # s[0,2] == ps[1,3]
                for s in possible_states[cur_state]:
                    for rs in range(16):
                        if (s & 5) == ((rs & 10)>>1):
                            cur_counts[j][s] += cur_counts[j+1][rs]
            elif j == y:
                # lower
                # s[0,1] == ps[2,3]
                for s in possible_states[cur_state]:
                    for ls in range(16):
                        if (s & 3) == ((ls & 12)>>2):
                                cur_counts[j][s] += pre_counts[j][ls]
            else:
                for s in possible_states[cur_state]:
                    # lower right
                    for lrs in range(16):
                        # right
                        # s[0,2] == ps[1,3]
                        for rs in range(16):
                            # lower
                            # s[0,1] == ps[2,3]
                            for ls in range(16):
                                if (s & 5) == ((rs & 10)>>1) and \
                                    (s & 3) == ((ls & 12)>>2) and \
                                    (rs & 3) == ((lrs & 12)>>2) and \
                                    (ls & 5) == ((lrs & 10)>>1):
                                    cur_counts[j][s] += min(cur_counts[j+1][rs], pre_counts[j][ls], pre_counts[j+1][lrs])

        pre_counts = cur_counts

    return sum(pre_counts[0].values())


def solution_tune1(states):
    true_states = (1, 2, 4, 8)
    false_states = (0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15)
    possible_states = {True: true_states, False: false_states}

    # start from lower right corner
    x = len(states)-1
    y = len(states[0])-1
    count = 0
    solution_stacks = []
    for _ in range(x+1):
        stacks = []
        for _ in range(y+1):
            stacks.append([])
        solution_stacks.append(stacks)
    if states[x][y] == True:
        solution_stacks[x][y] = list(true_states)
    else:
        solution_stacks[x][y] = list(false_states)
    
    while True:
        if x == y == 0:
            # solution found
            count += len(solution_stacks[x][y])
            solution_stacks[x][y] = []
            y = 1
            solution_stacks[x][y].pop()
        elif len(solution_stacks[x][y]) == 0:
            # poping stage
            if y < len(states[0])-1:
                y += 1
            elif x < len(states)-1:
                x += 1
                y = 0
            else:
                return count
            solution_stacks[x][y].pop()
        else:
            #==pushing stage==
            curss = []
            # right most column
            if y == 0:
                x -= 1
                y = len(states[0])-1
                cstate = states[x][y]
                bsolution = solution_stacks[x+1][y][-1]
                lobits = bsolution >> 2
                if cstate and lobits == 3:
                    x += 1
                    solution_stacks[x][y].pop()
                    continue
                # ??bb
                ps = possible_states[cstate]
                curss = []
                for i in [0, 4, 8, 12]:
                    s = i | lobits
                    if s in ps:
                        curss.append(s)
            # last row
            elif x == len(states)-1:
                y -= 1
                cstate = states[x][y]
                rsolution = solution_stacks[x][y+1][-1]
                rbits = (rsolution >> 1) & 5
                # ?b?b
                ps = possible_states[cstate]
                curss = []
                for i in [0, 2, 8, 10]:
                    s = i | rbits
                    if s in ps:
                        curss.append(s)
            else:
                y -= 1
                cstate = states[x][y]
                rsolution = solution_stacks[x][y+1][-1]
                bsolution = solution_stacks[x+1][y][-1]
                lrbits = ((rsolution >> 1) & 5) | (bsolution >> 2)
                # ?bbb
                ps = possible_states[cstate]
                curss = []
                if cstate and (bsolution >> 2) == 3:
                    x += 1
                    solution_stacks[x][y].pop()
                    continue
                for i in [0, 8]:
                    s = i | lrbits
                    if s in ps:
                        curss.append(s)

            solution_stacks[x][y] = curss

def solution_ori(states):
    true_states = (1, 2, 4, 8)
    false_states = (0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15)

    # relationship below
    # x blow y
    below = lambda x, y: ((x & 12) >> 2) == (y & 3)
    fbt = list((f, t) for t in true_states for f in false_states if below(f,t))
    fbf = list((f1, f2) for f2 in false_states for f1 in false_states if below(f1, f2))
    tbt = list((t1, t2) for t2 in true_states for t1 in true_states if below(t1, t2))
    tbf = list((t, f) for f in false_states for t in true_states if below(t, f))

    def get_rdict(relationship):
        d = {}
        for r in relationship:
            if r[0] in d:
                d[r[0]].add(r[1])
            else:
                d[r[0]] = set()
                d[r[0]].add(r[1])
        return d

    b_relationship = {
        (True, False): get_rdict(tbf),
        (False, False): get_rdict(fbf),
        (True, True): get_rdict(tbt),
        (False, True): get_rdict(fbt)
    }
    # right
    # x to the right of y
    right = lambda x, y: (y & 5) == ((x & 10) >> 1)
    frt = list((f, t) for t in true_states for f in false_states if right(f,t))
    frf = list((f1, f2) for f2 in false_states for f1 in false_states if right(f1, f2))
    trt = list((t1, t2) for t2 in true_states for t1 in true_states if right(t1, t2))
    trf = list((t, f) for f in false_states for t in true_states if right(t, f))

    r_relationship = {
        (True, False): get_rdict(trf),
        (False, False): get_rdict(frf),
        (True, True): get_rdict(trt),
        (False, True): get_rdict(frt)
    }

    # lowerright
    # lowerright = lambda x, y: (y & 1) == ((x & 8) >> 3)
    # lr_relationship = {
    #     (True, False): get_rdict(list((t, f) for f in false_states for t in true_states if lowerright(t, f))),
    #     (False, False): get_rdict(list((f1, f2) for f2 in false_states for f1 in false_states if lowerright(f1, f2))),
    #     (True, True): get_rdict(list((t1, t2) for t2 in true_states for t1 in true_states if lowerright(t1, t2))),
    #     (False, True): get_rdict(list((f, t) for t in true_states for f in false_states if lowerright(f,t)))
    # }

    # move to lower right corner
    x = len(states)-1
    y = len(states[0])-1
    count = 0
    solution_stacks = []
    for _ in range(x+1):
        stacks = []
        for _ in range(y+1):
            stacks.append([])
        solution_stacks.append(stacks)
    if states[x][y] == True:
        solution_stacks[x][y] = list(true_states)
    else:
        solution_stacks[x][y] = list(false_states)
    
    while True:
        if x == y == 0:
            # solution found
            count += len(solution_stacks[x][y])
            solution_stacks[x][y] = []
            y = 1
            solution_stacks[x][y].pop()
        elif len(solution_stacks[x][y]) == 0:
            # poping stage
            if y < len(states[0])-1:
                y += 1
            elif x < len(states)-1:
                x += 1
                y = 0
            else:
                return count
            solution_stacks[x][y].pop()
        else:
            # pushing stage
            # current solutions
            curss = set()
            if y > 0:
                rstate = states[x][y]
                rsolution = solution_stacks[x][y][-1]
                y -= 1
                cstate = states[x][y]
                rdict = r_relationship.get((rstate, cstate))
                if rsolution in rdict:
                    curss = rdict[rsolution]
                else:
                    y += 1
                    solution_stacks[x][y].pop()
                    continue

                # if x < len(states)-1:
                #     lrstate = states[x+1][y+1]
                #     lrsolution = solution_stacks[x+1][y+1][-1]
                #     lrdict = lr_relationship.get((lrstate, cstate))
                #     if lrsolution not in lrdict:
                #         x += 1
                #         y += 1
                #         solution_stacks[x][y].pop()
                #         continue
                #     else:
                #         curss = curss.intersection(lrdict.get(lrsolution))
            else:
                x -= 1
                y = len(states[0])-1
                cstate = states[x][y]
                if cstate:
                    curss = set(true_states)
                else:
                    curss = set(false_states)

            if x < len(states)-1:
                bstate = states[x+1][y]
                bsolution = solution_stacks[x+1][y][-1]
                bss = set()
                bdict = b_relationship.get((bstate, cstate))
                if bsolution in bdict:
                    bss = bdict[bsolution]
                # rewind the whole row if state is not possible
                if len(bss) == 0:
                    x += 1
                    solution_stacks[x][y].pop()
                    continue
                else:
                    curss = curss.intersection(bss)
            
            # validate curss against upper, left and upperleft cells
            if y > 0:
                vs = set()
                lstate = states[x][y-1]
                ldict = r_relationship.get((cstate, lstate))
                for s in curss:
                    if s in ldict:
                        vs.add(s)
                curss = vs
            if x > 0:
                vs = set()
                ustate = states[x-1][y]
                udict = b_relationship.get((cstate, ustate))
                for s in curss:
                    if s in udict:
                        vs.add(s)
                curss = curss.intersection(vs)

            solution_stacks[x][y] = list(curss)


# reference solution from https://gist.github.com/lotabout/891621ae8a01d8e512afd4b5254516b4
def generate(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

from collections import defaultdict
def build_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            generation = generate(i,j,n)
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping

def solution_ref(g):
    g = list(zip(*g)) # transpose
    nrows = len(g)
    ncols = len(g[0])

    # turn map into numbers
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = build_map(ncols, nums)

    preimage = {i: 1 for i in range(1<<(ncols+1))}
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret

def test_solution1():
    s2 = solution_ref([[True, False, True], [False, True, False], [True, False, True]])
    assert(s2==4)

def test_solution2():
    s1 = solution_ref([[True, True, False, True, False, True, False, True, True, False], 
                  [True, True, False, False, False, False, True, True, True, False],
                  [True, True, False, False, False, False, False, False, False, True], 
                  [False, True, False, False, False, False, True, True, False, False]])
    assert(s1==11567)

def test_solution3():
    s3 = solution_ref([[True, False, True, False, False, True, True, True], 
                   [True, False, True, False, False, False, True, False], 
                   [True, True, True, False, False, False, True, False], 
                   [True, False, True, False, False, False, True, False], 
                   [True, False, True, False, False, True, True, True]])
    assert(s3==254)

def test_rand():
    import random
    g = list(list(random.choice((True, False)) for _ in range(50)) for _ in range(9))
    #s = solution(g)
    s1 = solution_ref(g)
    assert(0==s1)