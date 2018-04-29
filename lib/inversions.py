def count_inversions(input):
    """ Recursive function that returns the number of inversions in the given
    array.

    This function creates a copy of the original input array that includes the
    original indexes. It then proceeds to use mergesort for sorting this array,
    while counting the inversions each time two parts are merged.

    Complexity of this function is O(n log_n).

    This function will run into the recursion limit for input arrays larger
    than 2^sys.getrecursionlimit(), which on most systems is way beyond what is
    computationally tractable.

    This function allocates about O(4n) extra memory; a copy of each original
    element and its index, and a temp buffer for sorted elements including
    original indexes.

    :param input: input array
    :return: int
    """
    # shadow input
    input = [(input[idx], idx) for idx in range(len(input))]

    def run(start, end):
        if end - start <= 1:
            return 0
        numinversions = 0
        # divide in center
        newend = (end + start) // 2
        # add number of inversions on the left side of the pivot
        numinversions += run(start, newend)
        # add number of  inversions on the right side opf the pivot
        numinversions += run(newend, end)
        # compare sorted arrays oon the left and right side...
        i, j, buf = start, newend, []
        while True:
            if input[i][0] <= input[j][0]:
                # if right is greater than left just add it to the sorted buffer
                buf.append(input[i])
                i += 1
                if i == newend:
                    # if we have no more elements left on the left, we add all
                    # remaining elements on the right to the buffer.
                    buf.extend(input[j:end])
                    break
            else:
                # if left is greater than right, than all sunsequent entries on
                # the left must also be greater than right so we count all.
                numinversions += newend - i
                buf.append(input[j])
                j += 1
                if j == end:
                    # if we have no more elements left on the right, we add all
                    # remaining elements on the left to the buffer.
                    buf.extend(input[i:newend])
                    break
        # overwrite the processed slice of the input
        input[start:end] = buf
        return numinversions

    return run(0, len(input))


if __name__ == '__main__':
    import random
    input = [random.randint(0, 2**17) for _ in range(2**17)]
    print(count_inversions(input))
