from __future__ import print_function
import numpy as np
from itertools import combinations, permutations


def kendalltau_dist(rank_a, rank_b):
    tau = 0
    n_candidates = len(rank_a)
    #rank_a[i] 代表字母的大小
    # 如果一个字母和另一个没关系，那它的数值为99,一个很大的数值

    for i, j in combinations(range(n_candidates), 2):
        #print(i,j)
        if rank_a[i]==99 or rank_a[j]==99 or rank_b[i]==99 or rank_b[j]==99:

            tau+=1
        else:

            if (np.sign(rank_a[i] - rank_a[j]) ==
                    np.sign(rank_b[i] - rank_b[j])):
                tau+=0
            else:
                tau+=2


    #print('**********')
    return tau


cols = "a b c d".split()


ranks = np.array([[0, 1, 2, 3],
                  [0, 1, 3, 2],
                  [0, 1, 2, 0],
                  [0, 1, 0, 2],
                  [0, 1, 3, 2]])

def rankaggr_brute(ranks):
    min_dist = np.inf
    best_rank = None
    n_voters, n_candidates = ranks.shape
    counter=0
    for candidate_rank in permutations(range(n_candidates)):
        counter+=1
        #print(counter)
        #print(candidate_rank)
        #print('***************')
        dist = np.sum(kendalltau_dist(candidate_rank, rank) for rank in ranks)
        if dist < min_dist:
            min_dist = dist
            best_rank = candidate_rank
    return min_dist, best_rank

if   __name__ == '__main__':
    dist, aggr = rankaggr_brute(ranks)
    print("A Kemeny-Young aggregation with score {} is: {}".
          format(dist, ", ".join(cols[i] for i in np.argsort(aggr))))




