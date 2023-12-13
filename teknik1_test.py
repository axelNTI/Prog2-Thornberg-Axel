import random
import time


def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    if arr[0] > arr[mid]:
        arr[0], arr[mid] = arr[mid], arr[0]
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    if arr[mid] > arr[-1]:
        arr[mid], arr[-1] = arr[-1], arr[mid]
    pivot = arr[mid]
    less, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return quicksort(less) + equal + quicksort(greater)


def slowsort(lista, sidor):
    slag = len(lista)
    sorteradlista = []
    bas = 1
    for y in range(sidor):
        sorteradlista.append(bas)
        bas = bas + 1
    for x in range(slag):
        tal = lista.pop(0)
        position = sorteradlista.index(tal)
        sorteradlista.insert(position, tal)
    bas2 = 1
    for z in range(sidor):
        sorteradlista.remove(bas2)
        bas2 = bas2 + 1
    return sorteradlista


sidor = 100
size = 100


quick_times = []
slow_times = []
for i in range(100):
    print(i)
    random_array = [random.randint(1, sidor) for _ in range(size)]

    quick_list = random_array.copy()
    quick_start = time.perf_counter_ns()
    quicksort(quick_list)
    quick_end = time.perf_counter_ns()
    quick_times.append(quick_end - quick_start)

    slow_list = random_array.copy()
    slow_start = time.perf_counter_ns()
    slowsort(slow_list, sidor)
    slow_end = time.perf_counter_ns()
    slow_times.append(slow_end - slow_start)

print(sum(quick_times) / len(quick_times))
print(sum(slow_times) / len(slow_times))
