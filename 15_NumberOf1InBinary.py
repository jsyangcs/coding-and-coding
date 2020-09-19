class Solution:
    def solve1(self, num):
        mask = 1
        cnt = 0
        while num:
            if mask & num:
                cnt += 1
            num >>= 1
        return cnt

    def solve2(self, num):
        cnt = 0
        while num:
            num &= (num-1)
            cnt += 1
        return cnt


def test():
    s = Solution()
    assert s.solve1(9) == 2
    assert s.solve1(1) == 1
    assert s.solve1(8) == 1
    assert s.solve1(0) == 0
    assert s.solve2(9) == 2
    assert s.solve2(1) == 1
    assert s.solve2(8) == 1
    assert s.solve2(0) == 0


if __name__ == '__main__':
    test()
