# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        
        lhs = []
        rhs = []

        for line in self.input:
            a,b = map(int, line.split())
            lhs.append(a)
            rhs.append(b)

        self.debug(lhs)
        self.debug(rhs)
        
        lhs.sort()
        rhs.sort()

        self.debug(lhs)
        self.debug(rhs)

        total_difference = sum(abs(a - b) for a,b in zip(lhs,rhs))

        return total_difference

    # @answer(1234)
    def part_2(self) -> int:

        lhs = []
        rhs = []

        for line in self.input:
            a,b = map(int, line.split())
            lhs.append(a)
            rhs.append(b)

        self.debug(lhs)
        self.debug(rhs)

        similarity_score = 0

        for element in lhs:
            similarity_score += element * rhs.count(element)

        return similarity_score

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
