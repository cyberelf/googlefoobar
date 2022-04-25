# Notes

Tips:

1. Start from the lower right cell.
    - If it's True, there will be 4 possible initial states.
    - If it's False, there will be 1(zero True)+4(three True)+6(2 True)=11 possible states.
2. Number all the states
    - For True

        ```bash
          0:    1:    2:    3:
          o.    .o    ..    ..
          ..    ..    o.    .o
        ```

    - For False

        ```bash
          0:    1:    2:    3:    4:    5:    6:    7:    8:    9:    10:
          ..    .o    o.    oo    oo    oo    o.    o.    .o    .o    ..
          ..    oo    oo    .o    o.    ..    o.    .o    o.    .o    oo
        ```

3. Find all state matches for all conjunction blocks.
    - True above False
        - T0-F0, T0-F10, T1-F0, T1-F10, T2-F2, T2-F6, T2-F7, T3-F1, T3-F8， T3-F9
    - True above True
        - T0-T2, T0-T3, T1-T2, T1-T3, T2-T0, T3-T1
    - False above True
        - F0-T2, F0-T3, F3-T1, F4-T0, F5-T2, F5-T3, F6-T0, F7-T1, F8-T0, F9-T1
    - True left False
        - 

4. Maintain a 3D array, with the first two dimensions as the input array, and the third dimension as a stack which stores all possible states.
5. Start from lower right cell, and set initial state_count to 0.
6. Push all possible states into the stack, if there is no available state, go to the former cell.
7. If current cell is the last one(upper left), pop all states and add them to state_count, then go to the former cell.
8. While there is nothing in stack, go to the former cell.
9. If the initial cell is empty, return state_count.
10. Pop one state from the current cell stack.
11. If there is a upper cell, move current cell pointer up. If not, move the pointer to the bottom of the left column.
12. If current cell is the last one(upper left), state count++ and go to the former cell, then goto step 8.
