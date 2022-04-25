
def solution(states):
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
                curss = curss.intersection(bss)
            solution_stacks[x][y] = list(curss)


def test_solution1():
    s2 = solution([[True, False, True], [False, True, False], [True, False, True]])
    assert(s2==4)

def test_solution2():
    s1 = solution([[True, True, False, True, False, True, False, True, True, False], 
                  [True, True, False, False, False, False, True, True, True, False],
                  [True, True, False, False, False, False, False, False, False, True], 
                  [False, True, False, False, False, False, True, True, False, False]])
    assert(s1==11567)

def test_solution3():
    s3 = solution([[True, False, True, False, False, True, True, True], 
                   [True, False, True, False, False, False, True, False], 
                   [True, True, True, False, False, False, True, False], 
                   [True, False, True, False, False, False, True, False], 
                   [True, False, True, False, False, True, True, True]])
    assert(s3==254)