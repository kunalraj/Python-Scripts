import itertools
 
left_right_map = {}
 
def equal_counts(tuple_of_tuples, weigh_cnt):
    # weigh_cnt == len(tuple_of_tuples[0])
    for i in range(weigh_cnt):
        left = sum([ 1 for x in tuple_of_tuples if x[i] == 1 ])
        right = sum([ 1 for x in tuple_of_tuples if x[i] == 2 ])
        if left != right:
            return False
    return True
 
def has_symmetric_coins(tuple_of_tuples, weigh_cnt):
    global left_right_map
    m = [ 0, 2, 1]
    if len(left_right_map) == 0:
        for t in itertools.product([0, 1, 2], repeat=weigh_cnt):
 
            equivalent_t = tuple([m[x] for x in t])
            left_right_map[t] = equivalent_t
    for t in tuple_of_tuples:
        equivalent_t = left_right_map[t]
        if equivalent_t in tuple_of_tuples:
            return True
    return False
 
def check(coins, weigh_cnt):
    pos = [ t for t in itertools.product([0, 1, 2], repeat=weigh_cnt)
            if sum(t) > 0 and sum(t) < weigh_cnt * 2 # remove no weighing and always right cases
          ]  
 
    i = 0
    sol = []
    for t in itertools.combinations(pos, coins):
 
        i += 1
        if i % 100000 == 0:
            print(i)
        if not equal_counts(t, weigh_cnt):
            continue
        if has_symmetric_coins(t, weigh_cnt):
            continue
        sol.append(t)
        print(i, len(sol), t)
    return sol
 
def is_unique_solution(tot, solutions, weigh_cnt):
    lrmaps = [[0, 1, 2], [ 0, 2, 1]] # 0: no change, 1: 1->2, 2->1
    for pm in itertools.permutations(range(weigh_cnt)):
        for lrmap in lrmaps:
            eqsol = []
            for t in tot:
                equivalent_t = tuple([ lrmap[t[pm[i]]] for i in range(weigh_cnt) ])
                eqsol.append(equivalent_t)
            eqsol.sort()
            eqsol = tuple(eqsol)
            if eqsol in solutions:
                return False
    return True
         
 
def main():
 
    COINS = 12
    COUNT = 3
    solutions = check(COINS, COUNT)
    uniq = []
    for sol in solutions:
        if is_unique_solution(sol, uniq, COUNT):
            uniq.append(sol)
    print(len(uniq))
    for u in uniq:
        print(u)
        for i in range(COUNT):
            print(i + 1, ":", [t[i] for t in u].count(0), end=", ")
        print()
 
if __name__ == "__main__":
    main()
