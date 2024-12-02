# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

import numpy as np
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    def is_report_safe(self, report: list[int]) -> bool:
        """
        Check if a report follows safety rules:
        - Numbers must be consistently either all increasing or all decreasing
        - Consecutive numbers must differ by 1-3
        """
        
        if len(report) < 2:
            return True
            
        differences = np.diff(report)
        signs = np.sign(differences)
        
        is_sequential = all(sign == signs[0] for sign in signs)
        has_valid_difference = all(1 <= abs(diff) <= 3 for diff in differences)
        
        return is_sequential and has_valid_difference

    def is_report_fixable(self, report: list[int]) -> bool:
        """
        Check if report can be made safe by removing one number.
        Returns True if removing any single number makes the report safe.
        """
        for i in range(len(report)):
            report_without_i = np.delete(report, i)
            if self.is_report_safe(report_without_i):
                return True
        return False

    @answer((631, 665)) # expected answers
    def solve(self) -> tuple[int, int]:
        safe_count = 0
        fixable_count = 0

        for line in self.input:
            report = [int(x) for x in line.split()]
            
            if self.is_report_safe(report):
                safe_count += 1
            elif self.is_report_fixable(report):
                fixable_count += 1

        return (safe_count, safe_count + fixable_count)