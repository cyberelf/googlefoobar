## Failed trials
I tried some simple ways to solve this problem and failed.
1. 2D iterative dynamic programming
Key to this problem is to find the number of unique combinations of *s* states into *w* slots.
Use dynamic programming to calculate:
 $S_{i,0}=1$
 $S_{0,j}=j+1$
 $S_{i,j}=S_{i-1,j}+S_{i,j-1}$

2. 3D dynamic programming

## I give up
The answer can be found [here](https://stackoverflow.com/questions/42655813/algorithm-to-find-unique-non-equivalent-configurations-given-the-height-the-wi). As I expected, this is a problem related to Group Theory (Burnside's lemma [1](https://en.wikipedia.org/wiki/Burnside's_lemma) [2](https://zhuanlan.zhihu.com/p/80261375)).

[This one](https://cs.stackexchange.com/questions/69095/counting-total-number-of-non-equivalent-configurations-in-a-2-d-grid) gives a clearer answer.


> I ordered a book on Group Theroy after this quest.