import time
import csv
from enum import Enum
from random import randint

import insertion_sort

class Ordering(Enum):
    Unsorted = 1
    Sorted = 2
    RevSorted = 3

def benchmark(sorting_algorithm, input_list):
    start_time = time.perf_counter()
    sorting_algorithm(input_list)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return elapsed

def generate_list(ordering, length):
    l = [None] * length
    match ordering:
        case Ordering.Unsorted:
            for i in range(length):
                l[i] = randint(0, length*10)
        case Ordering.Sorted:
            for i in range(length):
                l[i] = i
        case Ordering.RevSorted:
            for i in range(length):
                l[i] = (length - i - 1)
    return l


if __name__ == "__main__":
    sizes = [500, 2500, 10000, 20000, 30000]
    orderings = [Ordering.Unsorted, Ordering.Sorted, Ordering.RevSorted]

    with open("isort.csv", mode="w") as isort_csv: 
        writer = csv.writer(isort_csv, delimiter=",")
        writer.writerow(["List Size", "Unsorted", "Sorted", "Reverse Sorted"])
        for size in sizes:
            times = []
            for ordering in orderings:
                times.append(benchmark(insertion_sort.sort, generate_list(ordering, size)))    
            writer.writerow([size] + times)

    
