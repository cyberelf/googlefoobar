## Preperation
I did some estimation (function `estimation` and `solution_between`) and use them as the validation function.

## First puzzle
### Intuition 1

I tried to find some other form of representation of sqrt(2), like this:

$$ \sqrt{x} = \sum _{n=0}^{\infty }\frac{\sqrt {\pi }}{2}\,{\frac {{a}^{\frac{1}{2}-n} \left( x-a\right)^{n}}{\Gamma\left( \frac{3}{2}-n \right)n! }}.$$



### Intuition 2
I tried to find some pattern in the decimal part, with function `find_repeat` and `count_ints`, but it didn't work either.

### Intuition 3
I found the official definition of the this sequence: "[A Beatty sequence, A001951](http://oeis.org/A001951)"

https://en.wikipedia.org/wiki/Beatty_sequence#Rayleigh_theorem

> From Clark Kimberling, Oct 17 2016: (Start)
We can generate A001951 and A001952 without using sqrt(2).
First write the even positive integers in a row:
  2   4   6   8   10   12   14 . . .
Then put 1 under 2 and add:
  2   4   6   8   10   12   14 . . .
  1
  3
Next, under 4, put the least positive integer that is not yet in rows 2 and 3;
it is 2; and add:
  2   4   6   8   10   12   14 . . .
  1   2
  3   6
Next, under the 6 in row 1, put the least positive integer not yet in rows 2 and 3;
it is 4, and add:
  2   4   6   8   10   12   14 . . .
  1   2   4
  3   6   10
Continue in this manner. (End)

### Intuition 4

Beatty sequence and Rayleigh's theorem is the answer to this question.

* https://en.wikipedia.org/wiki/Beatty_sequence#Rayleigh_theorem
* https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s?newreg=cb33d186ad14497e9324f81b55236b86

#### Beatty sequence
In mathematics, a Beatty sequence (or homogeneous Beatty sequence) is the sequence of integers found by taking the floor of the positive multiples of a positive irrational number.

#### Rayleigh theorem

@MISC {2053713,
    TITLE = {How to find $\sum_{i=1}^n\left\lfloor i\sqrt{2}\right\rfloor$ A001951 A Beatty sequence: a(n) = floor(n*sqrt(2)).},
    AUTHOR = {mercio (https://math.stackexchange.com/users/17445/mercio)},
    HOWPUBLISHED = {Mathematics Stack Exchange},
    NOTE = {URL:https://math.stackexchange.com/q/2053713 (version: 2020-02-10)},
    EPRINT = {https://math.stackexchange.com/q/2053713},
    URL = {https://math.stackexchange.com/q/2053713}
}

## Second puzzle
Floating point precision also affects the answer. Use `Decimal` to solve this.

## Others Notes about this question
https://towardsdatascience.com/dodge-the-lasers-fantastic-question-from-googles-hiring-challenge-72363d95fec

## Misc

check https://zhuanlan.zhihu.com/p/350764840

