import numpy as np


def safe_max(arr: list):
    if len(arr) <= 0:
        return -1
    return max(arr)


def main():
    visible_trees = 0

    data = np.genfromtxt('day8.txt', delimiter=1, dtype=int)
    for y in range(0, data.shape[0]):
        for x in range(0, data.shape[1]):
            current_height = data[y, x]
            if safe_max(data[y, :x]) < current_height or safe_max(data[y, x+1:]) < current_height or safe_max(data[:y, x]) < current_height or safe_max(data[y+1:, x]) < current_height:
                visible_trees += 1

    print(visible_trees)


if __name__ == '__main__':
    main()
