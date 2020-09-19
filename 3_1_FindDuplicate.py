def solution(numbers):
    if not numbers:
        return -1

    for number in numbers:
        if number < 0 or number >= len(numbers):
            return -1

    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                return numbers[i]
            # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
            temp = numbers[i]
            numbers[i] = numbers[numbers[i]]
            numbers[temp] = temp

    return -1


def main():
    numbers = [2, 3, 1, 0, 2, 5, 4]
    print(solution(numbers))


if __name__ == '__main__':
    main()