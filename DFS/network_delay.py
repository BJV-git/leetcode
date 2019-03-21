# logic: need to calculate how many times the hope is and the max time
# caz at the same time we can travel from a node to multiple in parallel

# only source node is the one who can send

# so lets just return the max and the if seen len == N
import collections

def nwk_dlay(times, N,K):
    d=collections.defaultdict(dict)
    seen = set()
    seen.add(K)

    for i in times:
        d[i[0]].update({i[1]:i[2]})
    print(d)
    # exit()

    def get(child):
        try:
            pillalu = [i for i in d[child].keys() if i not in seen]
            for i in pillalu:
                seen.add(i)




            res=[d[child][i] + get(i) for i in pillalu]



            if res:
                return max(res)
            else:
                return 0
        except:
            return 0

    ans = get(K)

    if ans!=0:

        return ans
    else:
        return -1

print(nwk_dlay([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]],
5,
5))