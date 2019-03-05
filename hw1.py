import pandas as pd

def main():
    X1 = 61
    Y1 = 68
    Z1 = [4, 19, 90]

    X2 = 55
    Y2 = 27
    Z2 = [4, 8, 9, 12, 29, 32, 40, 44, 45, 48, 50, 52]

    print(dsep(X1, Y1, Z1))
    print(dsep(X2, Y2, Z2))

def dsep(X, Y, Z):
    df = pd.read_csv('dag.txt', sep=' ')
    df.columns = df.columns.astype(int)
    # phase 1
    ancestors = []
    L = Z

    while L:
        v = L.pop()

        if v not in ancestors:
            parents = df[v]

            for pa in parents[parents == 1].index:
                L.append(pa)

        ancestors.append(v)

    # phase 2
    visited = []
    reachable = []

    L.append((X, -1))

    while L:
        node = L.pop()

        if node not in visited:
            v = node[0]
            parents = df[v]
            children = df.iloc[v - 1]

            if v not in Z:
                reachable.append(node[0])

            visited.append(node)

            if node[1] == 1 and v not in Z:
                for pa in parents[parents == 1].index:
                    L.append((pa, 1))

                for ch in children[children == 1].index:
                    L.append((ch, -1))

            elif node[1] == -1:
                if v not in Z:
                    for ch in children[children == 1].index:
                        L.append((ch, -1))

                if v in ancestors:
                    for pa in parents[parents == 1].index:
                        L.append((pa, 1))

    return Y not in reachable

main()
