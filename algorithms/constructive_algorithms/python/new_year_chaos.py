def NewYearChaos(queue):
    swaps = 0
    swapped = False

    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"

    # bubble sorting to find the answer
    for _ in range(0, len(queue) - 1):
        for j in range(0, len(queue) - 1):
            if queue[j] > queue[j + 1]:
                queue[j], queue[j + 1] = queue[j+1], queue[j]
                swaps += 1
                swapped = True

        if swapped:
            swapped = False
        else:
            break
    return swaps


if __name__ == '__main__':
    T = int(input().strip())

    for _ in range(T):
        n = int(input().strip())
        queue = [int(q) for q in input().strip().split(' ')]

        print(NewYearChaos(queue))
