from itertools import combinations_with_replacement
print([1 for x in combinations_with_replacement(range(1,9),4) if sum(x)==8])
