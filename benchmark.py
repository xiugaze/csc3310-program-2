import time
from enum import Enum
from random import randint


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
    l = generate_list(Ordering.Unsorted, 100000)
    print(l)
    
