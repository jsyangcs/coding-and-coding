def solution(numbers):
    if not numbers:
        return -1
    hash_table = [0] * len(numbers)
    for number in numbers:
        if hash_table[number]:
            return number
        hash_table[number] += 1
    return -1


def main():
    numbers = [2, 3, 1, 3, 5, 4]
    print(solution(numbers))


if __name__ == '__main__':
    main()
