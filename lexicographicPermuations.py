a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
from itertools import permutations
lst = list(permutations(a))
print("".join(map(str, lst[1000000 - 1])))