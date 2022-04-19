
def solution(w, h, s):
    # We are going to need the gcd for all pairs of numbers (a,b)
    # with a<= w and b <= h. So, let's compute them all.
    n = max(w, h)
    gcdTable = buildGCDTable(n)
    # We will also need the factorials of all numbers 1,2,...,max(w,h)
    factorialTable = buildFactorialTable(n)
    # Consider G=S_w\times S_h, acting on X=W\times H, where
    # W={1,2,...,w}, H={1,2,...,h}, S_w and S_h are the symmetric group
    # acting as permutations of W and H, respectively.
    # Each matrix is a function f\in S^X, f:X to S, where
    # S={1,2,...,s}.
    # G acts on S^X, by (gf)(x)=f(gx) for g\in G and f\in S^X.
    # We need to compute the orbits of G in S^X.
    # Polya's enumeration theorem, tell us how to obtain it
    # from the Cycle Index Polynomial of the group action.
    # See https://franklinvp.github.io/2020-06-05-PolyaFooBar/
    # for the formula.
    grid = 0
    for cpw in partitionsAndCycleCount(w, factorialTable):
        for cph in partitionsAndCycleCount(h, factorialTable):
            m = cpw[1] * cph[1]
            grid += m * (s ** sum([sum([gcd(i, j, gcdTable) for i in cpw[0]]) for j in cph[0]]))
    return str(grid // (factorial(w, factorialTable) * factorial(h, factorialTable)))


def test_solution():
    s1 = solution([[True, True, False, True, False, True, False, True, True, False], 
                  [True, True, False, False, False, False, True, True, True, False],
                  [True, True, False, False, False, False, False, False, False, True], 
                  [False, True, False, False, False, False, True, True, False, False]])
    assert(s1==11567)
    
    s2 = solution([[True, False, True], [False, True, False], [True, False, True]])
    assert(s2==4)
    
    s3 = solution([[True, False, True, False, False, True, True, True], 
                   [True, False, True, False, False, False, True, False], 
                   [True, True, True, False, False, False, True, False], 
                   [True, False, True, False, False, False, True, False], 
                   [True, False, True, False, False, True, True, True]])
    assert(s3==254)