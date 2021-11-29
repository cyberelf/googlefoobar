Key to this problem is to find the number of unique combinations of *s* states into *w* slots.
Use dynamic programming to calculate:
 $S_{i,0}=1$
 $S_{0,j}=j+1$
 $S_{i,j}=S_{i-1,j}+S_{i,j-1}$