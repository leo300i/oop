diglist = [1, 2, 3]


class Solution:
    def plusOne(digits: list) -> list:
        diglist.append(diglist[-1] + 1)
        diglist.remove(diglist[-2])
Solution.plusOne(diglist)
print(diglist)