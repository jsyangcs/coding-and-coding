def solution(matrix, number):
    if not matrix:
        return -1  # need more validation for case like [[]]?

    # rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row <= cols - 1 and col >= 0:
        if matrix[row][col] == number:
            return True
        elif matrix[row][col] > number:
            col -= 1
        else:
            row += 1

    return False


def main():
    grid = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 0
    print(solution(grid, target))


if __name__ == '__main__':
    main()
