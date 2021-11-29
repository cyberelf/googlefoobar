def solution(w, h, s):
    """
    :type w: int
    :type h: int
    :type s: int
    :rtype: string
    """
    row_states = calculate_states(w, s)
    return calculate_states(h, row_states)

def calculate_states(w, s):
    """Calculate one dimensional states"""
    states = [1] * w 
    for i in range(s-1):
        states[0] += 1
        for j in range(1, w):
            states[j] += states[j-1]
    print(states)
    return states[w-1]

if __name__=="__main__":
    print(solution(2,3,2))