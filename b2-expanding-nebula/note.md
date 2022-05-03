# Notes

Tips:

1. Start from the lower right cell.
    - If it's True, there will be 4 possible initial states.
    - If it's False, there will be 1(zero True)+4(three True)+6(2 True)=11 possible states.
2. Number all the states can be represented with a four bit number, which orders from upper left to lower right.
    - For True, it's 0001, 0010, 0100, 1000
    - For False, it's the remaining numbers from 0 to 15

3. Find all possible conjunction numbers.
4. Maintain a 3D array, with the first two dimensions as the input array, and the third dimension as a stack which stores all possible states.
5. Start from lower right cell, and set initial state_count to 0.
6. Push all possible states into the stack, if there is no available state, go to the former cell.
7. If current cell is the last one(upper left), pop all states and add them to state_count, then go to the former cell.
8. While there is nothing in stack, go to the former cell.
9. If the initial cell is empty, return state_count.
10. Pop one state from the current cell stack.
11. If there is a upper cell, move current cell pointer up. If not, move the pointer to the bottom of the left column.
12. If current cell is the last one(upper left), state count++ and go to the former cell, then goto step 8.


Tune:
1. Add lower right corner check. Not Necessary. Wrong, This is a dulicate work.
2. Add adjacent check when pushing in new solution. Improves a little.

Solution:
What I'm missing is the parallelization. The answer to this is to do the calculation column by column which will reduce the 
time complexity from $O(2^{(M\times N)})$ to $O(2^{(2\times N)}+M\times 2^N\times N)$ where M>N. Space complexity from $O(M\times N)$ to $O(2^N)$.
