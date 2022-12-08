import numpy as np


def count_trees(current_height, arr):
    cnt = 0
    for x in arr:
        cnt += 1
        if x >= current_height:
            break
    return cnt


def main():
    data = np.genfromtxt('day8.txt', delimiter=1, dtype=int)
    best_count = 0

    for y in range(0, data.shape[0]):
        for x in range(0, data.shape[1]):
            ch = data[y, x]
            cnt = count_trees(ch, list(reversed(data[y, :x])))
            cnt *= count_trees(ch, data[y, x+1:])
            cnt *= count_trees(ch, list(reversed(data[:y, x])))
            cnt *= count_trees(ch, data[y+1:, x])

            if cnt > best_count:
                best_count = cnt

    print(best_count)


if __name__ == '__main__':
    main()
