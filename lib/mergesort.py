def mergesort(input):
    """Perform mergesort in-place (allocates O(n) extra memory)"""
    def run(start, end):
        if end - start <= 1:
            return
        newend = (end + start) // 2
        run(start, newend)
        run(newend, end)
        i, j, buf = start, newend, []
        while True:
            if input[i] <= input[j]:
                buf.append(input[i])
                i += 1
                if i == newend:
                    buf.extend(input[j:end])
                    break
            else:
                buf.append(input[j])
                j += 1
                if j == end:
                    buf.extend(input[i:newend])
                    break
        input[start:end] = buf
    run(0, len(input))


if __name__ == '__main__':
    import random
    input = [random.randint(0, 10) for _ in range(10)]
    mergesort(input)
    print(input)
