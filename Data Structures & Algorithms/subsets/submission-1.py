"""
[2,3]
[[], [2], [3], [2,3]]
[[1], [1,2], [1,3], [1,2,3]]


"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subsets_remaining = self.subsets(nums[1:])
        first = nums[0]

        subsets_with = []
        for subset in subsets_remaining:
            subsets_with.append([first, *subset])

        return subsets_with + subsets_remaining


        