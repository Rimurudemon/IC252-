def permutations(cups, old_permutations):
    if (len(cups) == 0):
        return old_permutations
    p = []
    for i in range(1, len(cups)):
        g = str(cups[0]) + str(cups[i])
        if (g not in old_permutations and g not in p):
            p.append(g)
    return permutations(cups[1:], old_permutations + p)


sol = []


def recursion(n, solns, cups):
    if (len(cups)==2):
        if (cups[0] != 1 and cups[1] != 1):
            sol.append(solns + [cups])
        return

    p = permutations(cups, [])
    final_permutation = []
    for i in range(len(p)):
        if (str(n) not in p[i]):
            final_permutation.append(p[i])
    for i in range(len(final_permutation)):
        ll = solns.copy()
        ll.append([int(final_permutation[i][0]), int(final_permutation[i][1])])
        fc = cups.copy()
        fc.remove(int(final_permutation[i][0]))
        fc.remove(int(final_permutation[i][1]))
        ll.append(recursion(n - 1, ll, fc))


n = 0
colors = ["R", "G", "B","V","I","Y","O","P","M","W","cups","F","X","E","K"]


def main():
    global n
    n = int(input("number of cups: "))
    cups = []
    for i in range(1, n // 2 + 1):
        cups += [i, i]
    recursion(n // 2, [], cups)
    print("number of combinations if cups are taken identical", len(sol))
    print('saucers:')
    for i in range(n//2):
        print(' ', colors[n//2-i-1], end='')
        print('  ', end='')
    print()
    print("===============================================================")
    for s in sol:
        for grp in s:
            for i in grp:
                print(colors[i-1], end=" ")
            print("  ", end='')
        print()
    print("number of combinations if cups are taken identical", len(sol))


main()
