This quest looks like a [Set Cover](https://www.geeksforgeeks.org/set-cover-is-np-complete/) problem at the first glance, but it's a much simpler one. In comparison to its peer (quest 7) at the same level (level 4), this one looks like a bonus quest.
Solution is as following:
1. I need to let any *num_required* bunnies have keys to all the consoles, but no group of *(num_required - 1)* bunnies have all of them. That means for any key to a specific console, there must be exactly *(num_buns - num_required + 1)* bunnies to have it. Also it means that each key should have a different combination of bunnies.
2. Enumerate all combinations of *(num_buns - num_required + 1)* out of *num_buns* bunnies, and push a key ID to each combination sequentially.
3. Bingo.