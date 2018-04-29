import random


def quicksort(input):
    """Quicksort sorts by choosing a random pivot and giving it it's rightful
    place.

    Strategies for choosing a pivot are:
    * random
    * first or last
    * median of first, middle or last

    Runtime of quicksort is O(n log_n). Quicksort works in-place, with O(1)
    overhead.
    """
    def run(start, end):
        if end - start <= 1:
            return
        pivot = random.randint(start, end-1)
        input[start], input[pivot] = input[pivot], input[start]
        pivotidx = start
        for i in range(start+1, end):
            if input[i] < input[start]:
                pivotidx += 1
                input[pivotidx], input[i] = input[i], input[pivotidx]
        input[pivotidx], input[start] = input[start], input[pivotidx]
        run(start, pivotidx)
        run(pivotidx+1, end)
    run(0, len(input))


if __name__ == '__main__':
    input = [random.randint(0, 2**10) for _ in range(2**10)]
    print(input)
    quicksort(input)
    print(input)