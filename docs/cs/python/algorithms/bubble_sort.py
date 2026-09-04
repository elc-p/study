num_list = [7, 1, 4, 2]
n = len(num_list)

def bubble_sort(a, n):
    flag = 1
    i = 0
    while flag:
        flag = 0
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                flag = 1
        i += 1

    return a

print(bubble_sort(num_list, n))