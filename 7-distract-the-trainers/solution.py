def solution(banana_list):
    """
    :type banana_list: int[]
    :rtype: int
    """
    # Step 1: Make the conjunction matrixs
    n_trainers = len(banana_list)
    match_graph = [ [0]*n_trainers for i in range(n_trainers)]
    for i in range(n_trainers):
        for j in range(i, n_trainers):
            match_graph[i][j] = match_graph[j][i] = match_on(banana_list[i], banana_list[j])
    
    # Step 2: blossom
    blossom = Blossom(match_graph)
    m = blossom.get_max_match()
    return n_trainers-2*m

# Part 1: matching 
def match_on(x, y):
    assert((x|y) != 0)
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

#=== Part 2: blossom utilities ===
class Blossom:
    (CLEAN, CANDIDATE, MATCHED)= range(3)
    def __init__(self, graph):
        self.G = graph
        self.size = len(graph)
        self.g_match = [0] * (self.size+1)      # global matching list
        self.s_q = []                           # global candidate queue
        self.s_pre = [0] * (self.size+1)        # per search pre list
        self.s_fathers = []                     # father of the vertex
        self.s_mark = []                        # mark of the vertex
        self._lca_ts = 0
        self._lca_ts_list = [0] * (self.size+1)

    # LCA related methods
    def getf(self, x):
        if self.s_fathers[x] == x:
            return x
        else:
            self.s_fathers[x] = self.getf(self.s_fathers[x])
            return self.s_fathers[x]

    def lca(self, x, y):
        self._lca_ts += 1
        x = self.getf(x)
        y = self.getf(y)
        while self._lca_ts_list[x] != self._lca_ts:
            self._lca_ts_list[x] = self._lca_ts
            x = self.getf(self.s_pre[self.g_match[x]])
            if y:
                x, y = y, x
        return x
    
    def blossom(self, x, y, l):
        while self.getf(x) != l:
            self.s_pre[x] = y
            y = self.g_match[x]
            if self.s_mark[y] == self.MATCHED:
                self._mark_candidate(y)
            if self.getf(x) == x:
                self.s_fathers[x] = l
            if self.getf(y) == y:
                self.s_fathers[y] = l
            x = self.s_pre[y]

    def _match(self, x, y):
        self.g_match[x] = y
        self.g_match[y] = x
    
    def _mark_candidate(self, x):
        self.s_mark[x] = self.CANDIDATE
        self.s_q.append(x)

    # blossom with current vertex
    def augment(self, vertex):
        # init the per round variables
        self.s_fathers = list(range(self.size+1))
        self.s_pre = [0] * (self.size+1)
        self.s_mark = [self.CLEAN] * (self.size+1)
        self.s_q = [vertex]
        self.s_mark[vertex] = self.CANDIDATE
        head = 0

        while head < len(self.s_q):
            cur_vertex = self.s_q[head]
            head += 1
            # search all adjacent vertices for match or augmentation
            for v in range(len(self.G[cur_vertex-1])):
                if self.G[cur_vertex-1][v]:
                    v += 1
                    # same flower or even ring
                    if self.getf(cur_vertex) == self.getf(v) or self.s_mark[v] == self.MATCHED:
                        continue
                    if self.s_mark[v] == self.CLEAN:
                        self.s_mark[v] = self.MATCHED
                        self.s_pre[v] = cur_vertex
                        if self.g_match[v] == 0:
                            # augment and return
                            x = v
                            while x:
                                last = self.g_match[self.s_pre[x]]
                                self._match(x, self.s_pre[x])
                                x = last
                            return True
                        else:
                            # mark match for search
                            self._mark_candidate(self.g_match[v])
                    else:
                        # mark of v is CANDIDATE
                        lca = self.lca(cur_vertex, v)
                        self.blossom(cur_vertex, v, lca)
                        self.blossom(v, cur_vertex, lca)
        return False

    def get_max_match(self):
        count = 0
        for i in range(1, self.size+1):
            if not self.g_match[i] and self.augment(i):
                count += 1
        return count


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
    # for i in range(1, 100):
    #     for j in range(1, 100):
    #         #matches((i,j))
    #         if match_on(i,j):
    #             print((i,j)) 
    #matches((99,77))
    #
    print(solution(range(1, 10)))
    print(solution([1,1]))
    print(solution([1, 7, 3, 21, 13, 19]))

    