The solution of this quest contains two parts of algorithms:
1. Given two numbers, substract the larger number by the smaller one and add that to the smaller one:
   $$ x=2\times{x}, y=y-x \mid x<y$$
   tell if x and y will eventually become the same number.
2. Find the maximum number of pairs in a graph.

Solution of the 1st one, i.e. x will eventually equals to y: if and only if the two numnbers satisfy the following rule:
* Devide them with their GCD, and get two new numbers $x_r$ and $y_r$. See if the sum of the two number is power of 2: $(x_r+y_r)=2^n$, or the smaller one times power of 2: $(x_r+y_r)=\min(x_r, y_r)\times2^n$

Solution to the 2nd one is blossom algorithm, which is a path augmenting algorithm with blossoms(odd rings) for constructing maximum matchings on graphs. Refer the following materials for more detail.
* https://www.bilibili.com/video/BV1bE411d7Py?p=122
* https://blog.csdn.net/birdmanqin/article/details/100160999
* https://en.wikipedia.org/wiki/Blossom_algorithm


There are two other version of solutions on the internet, and both of them are shorter. Need further study:
* https://github.com/arinkverma/google-foobar/blob/master/4.2_distract_grauds.py
* https://replit.com/@dayfine/Distract-the-Guard-foobar

 They both use Hungarian algorithm instead of Blossom algorithm, that means this graph is bipartite.?