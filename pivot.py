class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        len_n = len(nums)
        pivot = 0
        for i in range(0, len_n):
            if i == 0: 
                left_sum = 0
                right_sum = sum(nums[i+1:])
                pivot = 0
            elif i > 0 and i != len_n:
                left_sum = sum(nums[:i])
                right_sum = sum(nums[i+1:])
                pivot = i
            else:
                left_sum = sum(nums[:i])
                right_sum = 0
                pivot = -1

            print(f"iter: {i}, res = {left_sum} | {right_sum}")
            if left_sum == right_sum:
                return pivot
        return -1

sol = Solution()
print(sol.pivotIndex([1,2,3]))