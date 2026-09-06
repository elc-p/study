num_list = [9, 1, 4, 2, 7, 3]
n = len(num_list)

def insertion_sort_g(a, n, g):
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] >v:
            a[j + g] = a[j]
            j -= g
        a[j+g] = v
    return a

def shell_sort(a, n):
    h = 1
    g = []
    while h < n:
        g.append(h)
        h = 3 * h + 1
        h += 1

    l = len(g) - 1
    for k in range(l,-1,-1):
        insertion_sort_g(a, n, g[k])

    return a

print(shell_sort(num_list, n))
