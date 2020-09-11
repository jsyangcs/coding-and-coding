import re


def solution(string):
    regex = re.compile(' ')
    result = regex.sub('%20', string)
    return result


def main():
    string = 'We are happy.'
    print(solution(string))


if __name__ == '__main__':
    main()