num_list = [7, 1, 4, 2]
n = len(num_list)

def selection_sort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    return a

print(selection_sort(num_list, n))
